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

### Error de inicio de sesión
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
- con los argumentos: username=<usuario>&password=<password_cifrada>

### Respuesta recibida tras iniciar sesión


## 2. Mis proyectos

## 3. Mis subproyectos

## 4. Flujo de actividad

## 5. Incidentes

## 6. Nuevo incidente

## 7. Completar incidencia (Ir a taxonomía)
![alt text](imagenes/Ir_taxonomia.png)
### ¿Que se recibe al entrar en esta sección?
```
GET /incidente/index/2 HTTP/1.1
Host: 172.20.48.129:8090
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://172.20.48.129:8090/evento/index/1
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: JSESSIONID=3454A8C9F02AF56B72FC6D78CF7C3E87; _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; _gat_UA-97814751-2=1; _gat_gtag_UA_97814751_2=1; _ga_55LR48RTVX=GS2.1.s1762429181$o1$g1$t1762430554$j59$l0$h0
Connection: keep-alive
```

## 8. Añadir amenaza

## 9. Vincular activo+

## 10. Rellenar formulario de dimensiones y guardar

## 11. Vincular control (para cada control existente)

## 12. Ir a conclusión

## 13. Rellenar formulario, guardar y cerrar

## 14. Recalcular (opción 1)

## 15. Recalcular (opción 2)

## 16. Cerrar sesión
