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

### Como iniciar sesión
```
POST /login/existUser HTTP/1.1
Host: 172.20.48.129:8090
Content-Length: 44
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: */*
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: http://172.20.48.129:8090
Referer: http://172.20.48.129:8090/login/auth
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Connection: keep-alive

username=Con_premium&password=UzUkZTM1Ym4%3D
```
- Se hace peticion POST a /login/existUser
- 

## 2. Mis proyectos

## 3. Mis subproyectos

## 4. Flujo de actividad

## 5. Incidentes

## 6. Nuevo incidente

## 7. Completar incidencia (Ir a taxonomía)
![alt text](imagenes/Ir_taxonomia.png)

## 8. Añadir amenaza

## 9. Vincular activo+

## 10. Rellenar formulario de dimensiones y guardar

## 11. Vincular control (para cada control existente)

## 12. Ir a conclusión

## 13. Rellenar formulario, guardar y cerrar

## 14. Recalcular (opción 1)

## 15. Recalcular (opción 2)

## 16. Cerrar sesión
