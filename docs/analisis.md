# Análsis del comportamiento lógico de eMARISMA

## Contenido
1. Inicio de sesión
2. Mis proyectos
3. Mis subproyectos
4. Flujo de actividad
5. Incidentes
6. Nuevo incidente
7. Completar incidencia (Ir a taxonomía)
8. Añadir amenaza
9. Vincular activo+
10. Rellenar formulario de dimensiones y guardar
11. Vincular control (para cada control existente)
12. Ir a conclusión
13. Rellenar formulario, guardar y cerrar
14. Recalcular (opción 1)
15. Recalcular (opción 2)
16. Cerrar sesión

## 1. Inicio de sesión
![alt text](image.png)
### ¿Que se recibe al entrar en esta sección?
#### Error de inicio de sesión
Al intentar capturar las peticiones desde Burpsuite, reCAPTCHA nos lanza el siguiente  error:

    &g-recaptcha-response=0cAFcWeA5ihZy-[...]W4GEaPwi&postUrl=%2Flogin%2Fauthenticate

#### Solución del error de reCAPTCHA
1. Instalación de certificado de Burpsuite: soluciona parte del problema. `&g-recaptcha-response=&postUrl=%2Flogin%2Fauthenticate` ahora recaptcha-response viene vacío.
2. TLS passthrough: `&g-recaptcha-response=0cAFcWeA4Y76O2xa[...]uwAnfk&postUrl=%2Flogin%2Fauthenticate` ahora la respuesta llega completa y con `authenticate`.

## 2. Mis proyectos

## 3. Mis subproyectos

## 4. Flujo de actividad

## 5. Incidentes

## 6. Nuevo incidente

## 7. Completar incidencia (Ir a taxonomía)

## 8. Añadir amenaza

## 9. Vincular activo+

## 10. Rellenar formulario de dimensiones y guardar

## 11. Vincular control (para cada control existente)

## 12. Ir a conclusión

## 13. Rellenar formulario, guardar y cerrar

## 14. Recalcular (opción 1)

## 15. Recalcular (opción 2)

## 16. Cerrar sesión