# Analisis de la base de datos de Marisma

## Base de datos de Analisis de Riesgos

### Operación "Recalcular Analisis de Riesgos"

1. Disparo (inicio del cálculo): La aplicacion cambia el estado del proyecto para avisar que va a empezar a calcular.
    - Se inserta en `audit_log` y se actualiza el `subproyecto`.
    ```sql
    -- CAMBIO DE ESTADO A "CALCULANDO"
    UPDATE subproyecto set ... estado_calculo='calculandoAR' ... where id=1
    INSERT into audit_log ... new_value='calculandoAR' ...
    ```
2. Calculo:
    La base de datos realiza toda la operación de calculo del AR.
    - La formula matemática: hibernate lanza la consulta que recupera los datos y hace el calculo matemático en el propio SELECT:
    ```sql
    select ..., 
    this_.IMPACTO_TOTAL * this_.VULNERABILIDAD / 100 as formula0_2_  -- ¡AQUÍ ESTÁ EL CÁLCULO!
    from analisis_riesgo this_ 
    inner join activo_amenaza ...
    ```
    - La llamada al procedimiento almacenado: la app verifica si existe un "Stored Procedure" donde se delega la parte pesada del cálculo:
    ```sql
    SELECT name ... FROM mysql.proc WHERE name like 'sp_analisisRiesgo'
    ```
    - Recoleccion de dimensiones: diferentes consultas `select ... from activo_amenaza_dimension` están buscando las dimensiones de seguridad para cada activo.
3. Reultado (guardado de datos): Encontramos diferentes UPDATE finales. Estos confirman que el cálculo terminó y se guardó.
    - Estado final: el calculo termina con el estado `faltaPDT` (falta plan de tratamiento).
    - Valores guardados:
    ```sql
    -- Se guarda el nuevo estado
    UPDATE subproyecto ... estado_calculo='faltaPDT' ...

    -- Se guardan los riesgos calculados (Vulnerabilidad 45.83, Riesgo 48.0)
    UPDATE analisis_riesgo set ... vulnerabilidad=45.833332, riesgo=48.0 ... where id=2
    UPDATE analisis_riesgo set ... vulnerabilidad=41.666664, riesgo=16.0 ... where id=11
    ```

### Buscando el `analisis_riesgo` correcto

```sql
SELECT 
    -- 1. Contexto
    sp.nombre AS nombre_proyecto,
    sp.last_updated AS fecha_ultimo_calculo, -- <--- Aquí está la fecha real
    
    -- 2. El Activo (Lo que buscamos)
    ac.id AS id_activo,  -- ¡Aquí verás el ID que te faltaba!
    ac.nombre AS nombre_activo,
    
    -- 3. El Riesgo (El dato del incidente)
    ami.nombre AS amenaza,
    ar.vulnerabilidad AS vulnerabilidad_actual,
    ar.impacto AS impacto_actual,
    ar.riesgo AS riesgo_residual_final

FROM analisis_riesgo ar
    -- Unimos hacia arriba para llegar al Activo y al Proyecto
    INNER JOIN activo_amenaza aa ON ar.activo_amenaza_id = aa.id
    INNER JOIN activo ac ON aa.activo_id = ac.id
    INNER JOIN amenaza_instanciada ami ON aa.amenaza_instanciada_id = ami.id
    INNER JOIN subproyecto sp ON ami.subproyecto_id = sp.id

WHERE 
    ar.deleted = 0 
    AND ac.deleted = 0
    
    -- FILTRO AMIGABLE: Busca por nombre en vez de ID
    -- El % significa "cualquier cosa" (como un asterisco)
    AND ac.nombre LIKE '%' 
    
ORDER BY ar.riesgo DESC;
```

| nombre_proyecto | fecha_ultimo_calculo | id_activo | nombre_activo | amenaza                                                        | vulnerabilidad_actual | impacto_actual | riesgo_residual_final |
| --------------- | -------------------- | --------- | ------------- | -------------------------------------------------------------- | --------------------- | -------------- | --------------------- |
| prueba 1        | 2025-11-21 13:11:46  | 1         | Prueba        | Acceso no autorizado                                           | 45.8333               | 60.0           | 48.0                  |
| prueba 1        | 2025-11-21 13:11:46  | 1         | Prueba        | Alteración de secuencia                                        | 37.5                  | 60.0           | 36.0                  |
| prueba 1        | 2025-11-21 13:11:46  | 1         | Prueba        | Fuego                                                          | 31.25                 | 20.0           | 20.0                  |
| prueba 1        | 2025-11-21 13:11:46  | 1         | Prueba        | Robo                                                           | 100.0                 | 100.0          | 20.0                  |
| prueba 1        | 2025-11-21 13:11:46  | 1         | Prueba        | Daños por agua                                                 | 31.25                 | 20.0           | 20.0                  |
| prueba 1        | 2025-11-21 13:11:46  | 1         | Prueba        | Uso no previsto                                                | 37.5                  | 100.0          | 20.0                  |
| prueba 1        | 2025-11-21 13:11:46  | 1         | Prueba        | Interrupción de otros servicios y suministros esenciales       | 50.0                  | 80.0           | 16.0                  |
| prueba 1        | 2025-11-21 13:11:46  | 1         | Prueba        | Manipulación de los equipos                                    | 18.75                 | 80.0           | 16.0                  |
| prueba 1        | 2025-11-21 13:11:46  | 1         | Prueba        | Desastres industriales                                         | 12.5                  | 80.0           | 16.0                  |
| prueba 1        | 2025-11-21 13:11:46  | 1         | Prueba        | Avería de origen físico o lógico                               | 50.0                  | 80.0           | 16.0                  |
| prueba 1        | 2025-11-21 13:11:46  | 1         | Prueba        | Corte del suministro eléctrico                                 | 41.6667               | 80.0           | 16.0                  |
| prueba 1        | 2025-11-21 13:11:46  | 1         | Prueba        | Ataque destructivo                                             | 37.5                  | 60.0           | 12.0                  |
| prueba 1        | 2025-11-21 13:11:46  | 1         | Prueba        | Desastres naturales                                            | 23.6111               | 20.0           | 4.0                   |
| prueba 1        | 2025-11-21 13:11:46  | 1         | Prueba        | Errores de mantenimiento / actualización de equipos (hardware) | 0.0                   | 20.0           | 4.0                   |
| prueba 1        | 2025-11-21 13:11:46  | 1         | Prueba        | Emanaciones electromagnéticas                                  | 50.0                  | 20.0           | 4.0                   |
