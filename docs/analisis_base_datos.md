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