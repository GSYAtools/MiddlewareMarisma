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
### Respuesta a la petición de carga de "Obtener Mis Proyectos"
```
HTTP/1.1 200 
X-Frame-Options: DENY
X-Application-Context: application:production:9003
Content-Type: application/json;charset=UTF-8
Date: Fri, 07 Nov 2025 11:36:59 GMT
Keep-Alive: timeout=20
Connection: keep-alive
Content-Length: 28

[{"nombre":"Prueba","id":1}]
```
```
HTTP/1.1 200 
X-Frame-Options: DENY
X-Application-Context: application:production:9003
Content-Type: application/json;charset=UTF-8
Date: Fri, 07 Nov 2025 11:36:59 GMT
Keep-Alive: timeout=20
Connection: keep-alive
Content-Length: 14

{"proyecto":1}
```

## 3. Mis subproyectos
### Respuesta a la petición de carga de "Obtener Proyecto"
```
HTTP/1.1 200 
X-Frame-Options: DENY
X-Application-Context: application:production:9003
Content-Type: application/json;charset=UTF-8
Date: Fri, 07 Nov 2025 11:44:38 GMT
Keep-Alive: timeout=20
Connection: keep-alive
Content-Length: 412

{"sEcho":null,"iTotalRecords":1,"iTotalDisplayRecords":1,"aaData":[[1,"prueba 1","Agricultura, ganaderia, silvicultura y pesca","Prueba 1","Modelo de Madurez de Ciberseguridad para Gemelos Digitales elaborado por el Industrial IoT Consortium en colaboración con el Digital Twin Consortium","2025-10-08T11:37:38Z","2025-11-07T08:11:51Z",5," <small><i class=\"icofont icofont-tree\"><\/i> Prueba &gt;<\/small>"]]}
```

## 4. Flujo de actividad
### Respuesta a la petición de carga de "Ir a Subproyecto"

## 5. Incidentes

## 6. Nuevo incidente
### ¿Que se recibe al entrar en esta sección?
```
GET /evento/detalle?type=nuevo&a=1&e=0 HTTP/1.1
Host: 172.20.48.129:8090
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://172.20.48.129:8090/evento/index/1
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=F929DEE0D51EB6F2E5C6CEDF693917CA; _gat_UA-97814751-2=1; _gat_gtag_UA_97814751_2=1; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762504143$j22$l0$h0
Connection: keep-alive
```
```
POST /j/collect?v=1&_v=j102&a=1929445183&t=pageview&_s=1&dl=http%3A%2F%2F172.20.48.129%2Fevento%2Fdetalle%3Ftype%3Dnuevo%26a%3D1%26e%3D0&ul=es&dt=eMarisma%20%5BAn%C3%A1lisis%5D&sr=2560x1080&vp=2552x954&_u=SACAAEABEAAAACAAI~&jid=359474725&gjid=1408727147&cid=1791792627.1762429181&uid=con_premium&tid=UA-97814751-2&_gid=1977960298.1762429181&_r=1&_slc=1&gtm=45He5b50n81W72M73Xza200&cd1=con_premium&gcd=13l3l3l2l1l1&dma_cps=syphamo&dma=1&tag_exp=101509157~103116026~103200004~103233427~104527907~104528501~104684208~104684211~104948813~105446120~115480709~115583767~115938465~115938469~116194002~116217636~116217638&npa=1&z=1059090200 HTTP/2
Host: www.google-analytics.com
Content-Length: 0
Sec-Ch-Ua-Platform: "Windows"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Sec-Ch-Ua: "Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"
Content-Type: text/plain
Sec-Ch-Ua-Mobile: ?0
Accept: */*
Origin: http://172.20.48.129:8090
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Sec-Fetch-Storage-Access: active
Referer: http://172.20.48.129:8090/
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Priority: u=1, i
```
```
POST /sugerencia/cargarSugerencias/1 HTTP/1.1
Host: 172.20.48.129:8090
Content-Length: 0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: */*
X-Requested-With: XMLHttpRequest
Origin: http://172.20.48.129:8090
Referer: http://172.20.48.129:8090/evento/detalle?type=nuevo&a=1&e=0
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=F929DEE0D51EB6F2E5C6CEDF693917CA; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762504209$j60$l0$h0; _gat_UA-97814751-2=1
Connection: keep-alive
```
```
GET /subproyecto/obtenerProyecto/1 HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: */*
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/evento/detalle?type=nuevo&a=1&e=0
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=F929DEE0D51EB6F2E5C6CEDF693917CA; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762504209$j60$l0$h0; _gat_UA-97814751-2=1
Connection: keep-alive
```
```
GET /proyecto/obtenerMisProyectos/ HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/evento/detalle?type=nuevo&a=1&e=0
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=F929DEE0D51EB6F2E5C6CEDF693917CA; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762504209$j60$l0$h0; _gat_UA-97814751-2=1
Connection: keep-alive
```
```
POST /g/collect?v=2&tid=G-55LR48RTVX&gtm=45je5b50v9126092883za200&_p=1762504209515&gcd=13l3l3l2l3l1&npa=1&dma_cps=syphamo&dma=1&ul=es&sr=2560x1080&cid=1791792627.1762429181&are=1&frm=0&pscdl=noapi&_eu=ABAIAAQ&_s=1&tag_exp=101509157~103116026~103200004~103233427~104527907~104528500~104684208~104684211~104948813~105446120~115480709~115583767~115938465~115938469~116217636~116217638&dl=http%3A%2F%2F172.20.48.129%2Fevento%2Fdetalle%3Ftype%3Dnuevo%26a%3D1%26e%3D0&dt=eMarisma%20%5BAn%C3%A1lisis%5D&uid=con_premium&sid=1762499598&sct=2&seg=1&_tu=wAQ&en=page_view&_ee=1&ep.ua_dimension_1=con_premium&tfd=115450 HTTP/2
Host: region1.google-analytics.com
Content-Length: 0
Sec-Ch-Ua-Platform: "Windows"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Sec-Ch-Ua: "Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Accept: */*
Origin: http://172.20.48.129:8090
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: empty
Sec-Fetch-Storage-Access: active
Referer: http://172.20.48.129:8090/
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Priority: u=1, i
```
Al guardar:
```
POST /evento/save HTTP/1.1
Host: 172.20.48.129:8090
Content-Length: 159
Cache-Control: max-age=0
Origin: http://172.20.48.129:8090
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://172.20.48.129:8090/evento/detalle?type=nuevo&a=1&e=0
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=F929DEE0D51EB6F2E5C6CEDF693917CA; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762504260$j9$l0$h0
Connection: keep-alive

update=Guardar&id=&version=&subproyecto=1&tipo=detalle&typeAction=nuevo&responsable=Responsable1&date=21%2F11%2F2025&causa=Causa1&descripcion=Descripci%C3%B3n1
```
```
GET /evento/index/1 HTTP/1.1
Host: 172.20.48.129:8090
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://172.20.48.129:8090/evento/detalle?type=nuevo&a=1&e=0
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=F929DEE0D51EB6F2E5C6CEDF693917CA; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762504260$j9$l0$h0
Connection: keep-alive
```
```
POST /j/collect?v=1&_v=j102&a=918138403&t=pageview&_s=1&dl=http%3A%2F%2F172.20.48.129%2Fevento%2Findex%2F1&ul=es&dt=eMarisma%20%5BAn%C3%A1lisis%5D&sr=2560x1080&vp=2552x954&_u=SACAAEABEAAAACAAI~&jid=350215367&gjid=254149978&cid=1791792627.1762429181&uid=con_premium&tid=UA-97814751-2&_gid=1977960298.1762429181&_r=1&_slc=1&gtm=45He5b50n81W72M73Xza200&cd1=con_premium&gcd=13l3l3l2l1l1&dma_cps=syphamo&dma=1&tag_exp=101509157~103116026~103200004~103233427~104527907~104528500~104684208~104684211~104948813~105391253~115480709~115583767~115938466~115938468~116194002~116217636~116217638&npa=1&z=132497254 HTTP/1.1
Host: www.google-analytics.com
Content-Length: 0
Sec-Ch-Ua-Platform: "Windows"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Sec-Ch-Ua: "Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"
Content-Type: text/plain
Sec-Ch-Ua-Mobile: ?0
Accept: */*
Origin: http://172.20.48.129:8090
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Sec-Fetch-Storage-Access: active
Referer: http://172.20.48.129:8090/
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Priority: u=1, i
Connection: keep-alive
```
```
GET /evento/cargarEventoTabla/1?draw=1&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=false&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=6&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=7&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=&columns%5B8%5D%5Bname%5D=&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=false&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=1&order%5B0%5D%5Bdir%5D=asc&start=0&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1762504563290 HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/evento/index/1
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=F929DEE0D51EB6F2E5C6CEDF693917CA; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762504260$j9$l0$h0; _gat_UA-97814751-2=1
Connection: keep-alive
```
```
GET /user/serveImage?userInstance=4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
Referer: http://172.20.48.129:8090/evento/index/1
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=F929DEE0D51EB6F2E5C6CEDF693917CA; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762504260$j9$l0$h0; _gat_UA-97814751-2=1
Connection: keep-alive
```
```
GET /proyecto/obtenerMisProyectos/ HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/evento/index/1
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=F929DEE0D51EB6F2E5C6CEDF693917CA; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762504260$j9$l0$h0; _gat_UA-97814751-2=1
Connection: keep-alive
```
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
![alt text](imagenes/anadir_amenaza.png)
### Al pulsar el botón de guardar:
```
POST /incidente/guardarGravedad?gravedad=grave&incidente=3&subproyecto=1 HTTP/1.1
Host: 172.20.48.129:8090
Content-Length: 0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: */*
X-Requested-With: XMLHttpRequest
Origin: http://172.20.48.129:8090
Referer: http://172.20.48.129:8090/incidente/index/3
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762499999$j60$l0$h0
Connection: keep-alive
```
### Se accede a la taxonomía del incidente y carga toda la web
```
GET /incidente/cargarTablaControlesImplicados/1?incidente=0&draw=1&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=false&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=1&order%5B0%5D%5Bdir%5D=asc&start=0&length=-1&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1762504723766 HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/incidente/index/4
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=F929DEE0D51EB6F2E5C6CEDF693917CA; _gat_UA-97814751-2=1; _gat_gtag_UA_97814751_2=1; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762504723$j60$l0$h0
Connection: keep-alive
```
```
GET /incidente/cargarTablaActivosImplicados/1?incidente=0&draw=1&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=false&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=2&order%5B0%5D%5Bdir%5D=asc&start=0&length=-1&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1762504723764 HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/incidente/index/4
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=F929DEE0D51EB6F2E5C6CEDF693917CA; _gat_UA-97814751-2=1; _gat_gtag_UA_97814751_2=1; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762504723$j60$l0$h0
Connection: keep-alive
```
```
GET /incidente/cargarTablaControlesNoImplicados/1?incidente=0&draw=1&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=false&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=false&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=1&order%5B0%5D%5Bdir%5D=asc&start=0&length=-1&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1762504723765 HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/incidente/index/4
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=F929DEE0D51EB6F2E5C6CEDF693917CA; _gat_UA-97814751-2=1; _gat_gtag_UA_97814751_2=1; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762504723$j60$l0$h0
Connection: keep-alive
```
```
GET /incidente/cargarTablaActivosNoImplicados/1?incidente=0&draw=1&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=false&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=false&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=false&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=&columns%5B8%5D%5Bname%5D=&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=9&columns%5B9%5D%5Bname%5D=&columns%5B9%5D%5Bsearchable%5D=false&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B10%5D%5Bdata%5D=&columns%5B10%5D%5Bname%5D=&columns%5B10%5D%5Bsearchable%5D=true&columns%5B10%5D%5Borderable%5D=false&columns%5B10%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B10%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=2&order%5B0%5D%5Bdir%5D=asc&start=0&length=-1&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1762504723763 HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/incidente/index/4
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=F929DEE0D51EB6F2E5C6CEDF693917CA; _gat_UA-97814751-2=1; _gat_gtag_UA_97814751_2=1; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762504723$j60$l0$h0
Connection: keep-alive
```
```
GET /proyecto/obtenerMisProyectos/ HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/incidente/index/4
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=F929DEE0D51EB6F2E5C6CEDF693917CA; _gat_UA-97814751-2=1; _gat_gtag_UA_97814751_2=1; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762504723$j60$l0$h0
Connection: keep-alive
```
```
GET /subproyecto/obtenerProyecto/1 HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: */*
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/incidente/index/4
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=F929DEE0D51EB6F2E5C6CEDF693917CA; _gat_UA-97814751-2=1; _gat_gtag_UA_97814751_2=1; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762504723$j60$l0$h0
Connection: keep-alive
```
```
POST /incidente/guardarAmenaza/170 HTTP/1.1
Host: 172.20.48.129:8090
Content-Length: 23
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: */*
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: http://172.20.48.129:8090
Referer: http://172.20.48.129:8090/incidente/index/4
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=F929DEE0D51EB6F2E5C6CEDF693917CA; _gat_UA-97814751-2=1; _gat_gtag_UA_97814751_2=1; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762504723$j60$l0$h0
Connection: keep-alive

gravedad=grave&evento=4
```

### JSON:
Donde pone vincular activo:
```
HTTP/1.1 200 
X-Frame-Options: DENY
X-Application-Context: application:production:9003
Content-Type: application/json;charset=UTF-8
Date: Fri, 07 Nov 2025 11:48:35 GMT
Keep-Alive: timeout=20
Connection: keep-alive
Content-Length: 1114

{"sEcho":null,"iTotalRecords":1,"iTotalDisplayRecords":1,"aaData":[[1,{"id":1,"estado":"cerrado","cobertura":0.0,"deleted":false,"exito":0.0,"respuestas":[{"id":1},{"id":69},{"id":14},{"id":62},{"id":41},{"id":6},{"id":22},{"id":45},{"id":32},{"id":2},{"id":9},{"id":48},{"id":59},{"id":52},{"id":56},{"id":20},{"id":57},{"id":42},{"id":11},{"id":49},{"id":25},{"id":61},{"id":53},{"id":50},{"id":46},{"id":21},{"id":37},{"id":4},{"id":24},{"id":30},{"id":64},{"id":60},{"id":31},{"id":28},{"id":29},{"id":16},{"id":19},{"id":63},{"id":5},{"id":18},{"id":15},{"id":54},{"id":27},{"id":68},{"id":12},{"id":51},{"id":70},{"id":35},{"id":10},{"id":40},{"id":39},{"id":38},{"id":55},{"id":23},{"id":43},{"id":8},{"id":13},{"id":26},{"id":65},{"id":67},{"id":17},{"id":36},{"id":58},{"id":34},{"id":71},{"id":44},{"id":33},{"id":3},{"id":7},{"id":66},{"id":47}],"nombreGrupoActivos":"Grupo General","incidentesActivo":[{"id":1},{"id":4},{"id":2},{"id":3}],"subproyecto":{"id":1},"activosAuditoria":[{"id":1}],"nombre":"Agrupación CHKL_General [prueba 1]"},"Equipamiento auxiliar","Prueba",null,null,null,null,1,null]]}
```
Donde pone vincular control:
```
HTTP/1.1 200 
X-Frame-Options: DENY
X-Application-Context: application:production:9003
Content-Type: application/json;charset=UTF-8
Date: Fri, 07 Nov 2025 11:48:35 GMT
Keep-Alive: timeout=20
Connection: keep-alive
Content-Length: 4855

{"sEcho":null,"iTotalRecords":18,"iTotalDisplayRecords":18,"aaData":[[55,"CMM-01-01-01","Programa de Gestión de la Seguridad","Esta práctica restringe los tipos de cambios permitidos, cuándo se pueden realizar esos cambios, los procesos de aprobación y cómo manejar los escenarios de cambios de emergencia.",null],[56,"CMM-01-01-02","Gestión del Cumplimiento","Esta práctica es necesaria cuando se necesitan requisitos estrictos para el cumplimiento de los estándares de seguridad en evolución.",null],[57,"CMM-01-02-01","Modelado de Amenazas","Esta práctica tiene como objetivo revelar los factores conocidos y específicos que pueden poner en riesgo el funcionamiento de un sistema dado y describir con precisión estos factores.",null],[58,"CMM-01-02-02","Actitud frente al Riesgo","Esta práctica permite a una organización establecer una estrategia para hacer frente a los riesgos de acuerdo con la política de gestión de riesgos, incluidas las condiciones para la aceptación, evasión, evaluación, mitigación y transferencia.",null],[59,"CMM-01-03-01","Gestión de riesgos de la cadena de suministro de productos","Esta práctica tiene como objetivo revelar los factores conocidos y específicos que pueden poner en riesgo el funcionamiento de un sistema dado y describir con precisión estos factores.",null],[60,"CMM-01-03-02","Gestión de Servicios y Dependencias entre Terceros","Esta práctica aborda la necesidad de generar confianza para los socios y terceras partes. La capacidad de tener la seguridad de la confianza de terceros requiere la comprensión de la infraestructura comercial y de confianza y las posibles fuentes de amenazas ocultas.",null],[61,"CMM-02-01-01","Establecimiento y mantenimiento de identidades","Esta práctica ayuda a identificar y restringir quién puede acceder al sistema y sus privilegios.",null],[62,"CMM-02-01-02","Control de Accesos","La política y la implementación de esta práctica permiten que una empresa limite el acceso a los recursos solo a las identidades específicas que requieren acceso y solo al nivel específico necesario para cumplir con los requisitos de la organización.",null],[64,"CMM-02-02-01","Protección Física","Las políticas de esta práctica abordan la seguridad física y la protección de las instalaciones, su gente y los sistemas para evitar robos y garantizar la operación segura continua del equipo.",null],[63,"CMM-02-02-02","Gestión de activos, cambios y configuración","Esta práctica restringe los tipos de cambios permitidos, cuándo se pueden realizar esos cambios, los procesos de aprobación y cómo manejar los escenarios de cambios de emergencia.",null],[65,"CMM-02-03-01","Modelo y Política de Protección de Datos","Esta práctica identifica si existen diferentes categorías de datos y considera los objetivos y reglas específicas para la protección de datos.",null],[66,"CMM-02-03-02","Implementación de Prácticas de Protección de Datos","Esta práctica describe la aplicación preferida de los mecanismos de protección de datos para abordar la confidencialidad, la integridad y la disponibilidad.",null],[67,"CMM-03-01-01","Evaluación de Vulnerabilidades","Esta práctica ayuda a identificar vulnerabilidades, determinar el riesgo que cada vulnerabilidad supone para el organización y desarrollar un plan de remediación priorizado.",null],[68,"CMM-03-01-02","Gestión de Parches","Esta práctica aclara cuándo y con qué frecuencia aplicar los parches de software, establece procedimientos para parches de emergencia y propone mitigaciones adicionales en caso de acceso restringido al sistema u otros problemas relacionados con la aplicación de parches.",null],[69,"CMM-03-02-01","Prácticas de Monitorización","Esta práctica se utiliza para monitorear el estado del sistema, identificar anomalías y ayudar en la resolución de disputas.",null],[70,"CMM-03-02-02","Concienciación sobre el conexto e Intercambio de Información","Esta práctica ayuda a las organizaciones a estar mejor preparadas para responder a las amenazas. Compartir información sobre amenazas mantiene los sistemas actualizados.",null],[71,"CMM-03-03-01","Detección de Eventos y Plan de Respuestas","Esta práctica define qué es un evento de seguridad y cómo detectar y asignar eventos para su investigación, escalarlos según sea necesario y responder adecuadamente.\r\nTambién debe incluir un plan de comunicaciones para compartir información de manera adecuada y oportuna con las partes interesadas.",null],[72,"CMM-03.03-02","Remediación, Recuperación y Continuidad de Operaciones","Esta práctica es una combinación de redundancias técnicas en las que el personal capacitado y la política de continuidad comercial ayudan a una organización a recuperarse rápidamente de un evento para acelerar el regreso a la normalidad.",null]]}
```
## 9. Vincular activo
![alt text](imagenes/vincular_activo.png)
Al pulsar el botón "Vincular activo" nos va a llegar el endpoint que se muestra a continuación y después va a aparecer el cuadro de diálogo de Añadir Activo en el que vamos a tener que introducir las dimensiones. 
### ¿Que se recibe al entrar en esta sección?
```
GET /incidente/cargarDimensionesClear?activo=1&incidente=3 HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: */*
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/incidente/index/3
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762500456$j60$l0$h0
Connection: keep-alive
```

## 10. Rellenar formulario de dimensiones y guardar
![alt text](imagenes/formulario_dimensiones.png)
Al rellenar el porcentaje de autenticidad se ha recibido:
```
GET /incidente/vincularActivo?dimension=19&activo=&incidente=3&porcentaje=16&vincular=false&activoAux=1 HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: */*
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/incidente/index/3
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762500456$j60$l0$h0
Connection: keep-alive
```
Y al marcar la casilla de seleccionar carga de nuevo las tablas de controles y activos:
```
GET /incidente/cargarTablaControlesImplicados/1?incidente=3&draw=4&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=false&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=1&order%5B0%5D%5Bdir%5D=asc&start=0&length=-1&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1762500456161 HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/incidente/index/3
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762500456$j60$l0$h0
Connection: keep-alive
```
```
GET /incidente/cargarTablaControlesNoImplicados/1?incidente=3&draw=4&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=false&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=false&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=1&order%5B0%5D%5Bdir%5D=asc&start=0&length=-1&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1762500456159 HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/incidente/index/3
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762500456$j60$l0$h0
Connection: keep-alive
```
```
GET /incidente/cargarTablaActivosNoImplicados/1?incidente=3&draw=4&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=false&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=false&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=false&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=&columns%5B8%5D%5Bname%5D=&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=9&columns%5B9%5D%5Bname%5D=&columns%5B9%5D%5Bsearchable%5D=false&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B10%5D%5Bdata%5D=&columns%5B10%5D%5Bname%5D=&columns%5B10%5D%5Bsearchable%5D=true&columns%5B10%5D%5Borderable%5D=false&columns%5B10%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B10%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=2&order%5B0%5D%5Bdir%5D=asc&start=0&length=-1&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1762500456160 HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/incidente/index/3
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762500456$j60$l0$h0
Connection: keep-alive
```
Después de añadir las dimensiones obtenemos el JSON:
```
HTTP/1.1 200 
X-Frame-Options: DENY
X-Application-Context: application:production:9003
Content-Type: application/json;charset=UTF-8
Date: Fri, 07 Nov 2025 11:55:25 GMT
Keep-Alive: timeout=20
Connection: keep-alive
Content-Length: 1109

{"sEcho":null,"iTotalRecords":1,"iTotalDisplayRecords":1,"aaData":[[5,{"id":1,"estado":"cerrado","cobertura":0.0,"deleted":false,"exito":0.0,"respuestas":[{"id":64},{"id":66},{"id":2},{"id":21},{"id":43},{"id":4},{"id":11},{"id":20},{"id":14},{"id":10},{"id":53},{"id":30},{"id":47},{"id":68},{"id":29},{"id":62},{"id":56},{"id":65},{"id":36},{"id":50},{"id":23},{"id":41},{"id":5},{"id":25},{"id":44},{"id":28},{"id":59},{"id":57},{"id":67},{"id":16},{"id":32},{"id":1},{"id":9},{"id":40},{"id":13},{"id":12},{"id":46},{"id":69},{"id":3},{"id":49},{"id":48},{"id":51},{"id":52},{"id":6},{"id":26},{"id":70},{"id":24},{"id":31},{"id":38},{"id":61},{"id":27},{"id":33},{"id":34},{"id":35},{"id":7},{"id":17},{"id":19},{"id":60},{"id":42},{"id":45},{"id":54},{"id":63},{"id":15},{"id":39},{"id":22},{"id":55},{"id":58},{"id":8},{"id":71},{"id":37},{"id":18}],"nombreGrupoActivos":"Grupo General","incidentesActivo":[{"id":4},{"id":3},{"id":2},{"id":5},{"id":1}],"subproyecto":{"id":1},"activosAuditoria":[{"id":1}],"nombre":"Agrupación CHKL_General [prueba 1]"},"Equipamiento auxiliar","Prueba","[[A]]",null]]}
```
Para cerrar pulsamos el botón "Cerrar" y recargamos la página y al hacer esto nos aparecerían los endpoints anteriores y además la de activos implicados:
```
GET /incidente/cargarTablaActivosImplicados/1?incidente=3&draw=1&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=false&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=2&order%5B0%5D%5Bdir%5D=asc&start=0&length=-1&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1762501352234 HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/incidente/index/3
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762501352$j60$l0$h0
Connection: keep-alive
```
Y además, el endpoint de cargar sugerencias:
```
POST /sugerencia/cargarSugerencias/1 HTTP/1.1
Host: 172.20.48.129:8090
Content-Length: 0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: */*
X-Requested-With: XMLHttpRequest
Origin: http://172.20.48.129:8090
Referer: http://172.20.48.129:8090/incidente/index/3
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762501352$j60$l0$h0; _gat_UA-97814751-2=1
Connection: keep-alive
```

## 11. Vincular control (para cada control existente)
![alt text](imagenes/vincular_control.png)
### ¿Qué se recibe al entrar en esta sección?
```
GET /incidente/cargarTablaControlesImplicados/1?incidente=3&draw=2&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=false&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=1&order%5B0%5D%5Bdir%5D=asc&start=0&length=-1&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1762501352238 HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/incidente/index/3
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762501785$j60$l0$h0
Connection: keep-alive
```
```
GET /incidente/cargarTablaControlesNoImplicados/1?incidente=3&draw=2&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=false&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=false&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=1&order%5B0%5D%5Bdir%5D=asc&start=0&length=-1&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1762501352237 HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/incidente/index/3
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762501785$j60$l0$h0
Connection: keep-alive
```
JSON de controles implicados:
```
HTTP/1.1 200 
X-Frame-Options: DENY
X-Application-Context: application:production:9003
Content-Type: application/json;charset=UTF-8
Date: Fri, 07 Nov 2025 12:00:20 GMT
Keep-Alive: timeout=20
Connection: keep-alive
Content-Length: 318

{"sEcho":null,"iTotalRecords":1,"iTotalDisplayRecords":1,"aaData":[[55,"CMM-01-01-01","Programa de Gestión de la Seguridad","Esta práctica restringe los tipos de cambios permitidos, cuándo se pueden realizar esos cambios, los procesos de aprobación y cómo manejar los escenarios de cambios de emergencia.",null]]}
```
## 12. Ir a conclusión
![alt text](imagenes/ir_conclusion.png)
### ¿Qué se recibe al entrar en esta sección?
```
GET /evento/conclusion/3 HTTP/1.1
Host: 172.20.48.129:8090
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://172.20.48.129:8090/incidente/index/3
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762501785$j60$l0$h0
Connection: keep-alive
```
```
POST /j/collect?v=1&_v=j102&a=2126431393&t=pageview&_s=1&dl=http%3A%2F%2F172.20.48.129%2Fevento%2Fconclusion%2F3&ul=es&dt=eMarisma%20%5BAn%C3%A1lisis%5D&sr=2560x1080&vp=2552x954&_u=SACAAEABEAAAACAAI~&jid=462901624&gjid=2117804085&cid=1791792627.1762429181&uid=con_premium&tid=UA-97814751-2&_gid=1977960298.1762429181&_r=1&_slc=1&gtm=45He5b50n81W72M73Xza200&cd1=con_premium&gcd=13l3l3l2l1l1&dma_cps=syphamo&dma=1&tag_exp=101509157~103116026~103200004~103233427~104527907~104528501~104684208~104684211~104948813~115480710~115583767~115938465~115938468~116194002~116217636~116217638&npa=1&z=1141133975 HTTP/1.1
Host: www.google-analytics.com
Content-Length: 0
Sec-Ch-Ua-Platform: "Windows"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Sec-Ch-Ua: "Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"
Content-Type: text/plain
Sec-Ch-Ua-Mobile: ?0
Accept: */*
Origin: http://172.20.48.129:8090
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Sec-Fetch-Storage-Access: active
Referer: http://172.20.48.129:8090/
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Priority: u=1, i
Connection: keep-alive
```
```
GET /autofillservice/core/page/-231337821200553506/-6667012314416865225%7C-1646443967660173542%7C297014979059213897?CIdAlgoVersion=2 HTTP/1.1
Host: edge.microsoft.com
X-Client-Data: CKj/ygE=
Sec-Fetch-Site: none
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: empty
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Priority: u=4, i
Connection: keep-alive
```
## 13. Rellenar formulario, guardar y cerrar
![alt text](imagenes/guardar_cerrar.png)
### ¿Qué se recibe al entrar en esta sección?
```
POST /evento/save/3 HTTP/1.1
Host: 172.20.48.129:8090
Content-Length: 1187
Cache-Control: max-age=0
Origin: http://172.20.48.129:8090
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryVBepmDttZU1AThSV
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://172.20.48.129:8090/evento/conclusion/3
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _gat_gtag_UA_97814751_2=1; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762502460$j60$l0$h0
Connection: keep-alive

------WebKitFormBoundaryVBepmDttZU1AThSV
Content-Disposition: form-data; name="save"

Guardar
------WebKitFormBoundaryVBepmDttZU1AThSV
Content-Disposition: form-data; name="id"

3
------WebKitFormBoundaryVBepmDttZU1AThSV
Content-Disposition: form-data; name="version"

2
------WebKitFormBoundaryVBepmDttZU1AThSV
Content-Disposition: form-data; name="subproyecto"

1
------WebKitFormBoundaryVBepmDttZU1AThSV
Content-Disposition: form-data; name="tipo"

conclusion
------WebKitFormBoundaryVBepmDttZU1AThSV
Content-Disposition: form-data; name="cerrar"

true
------WebKitFormBoundaryVBepmDttZU1AThSV
Content-Disposition: form-data; name="coste"

0.00€
------WebKitFormBoundaryVBepmDttZU1AThSV
Content-Disposition: form-data; name="myCurrency"

EUR
------WebKitFormBoundaryVBepmDttZU1AThSV
Content-Disposition: form-data; name="solucion"

Solución
------WebKitFormBoundaryVBepmDttZU1AThSV
Content-Disposition: form-data; name="conclusion"

Conclusión
------WebKitFormBoundaryVBepmDttZU1AThSV
Content-Disposition: form-data; name="evidencias[]"; filename=""
Content-Type: application/octet-stream


------WebKitFormBoundaryVBepmDttZU1AThSV--
```
```
GET /evento/index/1 HTTP/1.1
Host: 172.20.48.129:8090
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://172.20.48.129:8090/evento/conclusion/3
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762502460$j60$l0$h0
Connection: keep-alive
```
Después de esto, cuando cierra lo anterior y carga la nueva página, aparecen los siguientes endpoints:
```
POST /sugerencia/cargarSugerencias/1 HTTP/1.1
Host: 172.20.48.129:8090
Content-Length: 0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: */*
X-Requested-With: XMLHttpRequest
Origin: http://172.20.48.129:8090
Referer: http://172.20.48.129:8090/evento/index/1
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762502460$j60$l0$h0; _gat_UA-97814751-2=1
Connection: keep-alive
```
```
GET /evento/cargarEventoTabla/1?draw=1&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=false&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=6&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=7&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=&columns%5B8%5D%5Bname%5D=&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=false&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=1&order%5B0%5D%5Bdir%5D=asc&start=0&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1762502595427 HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/evento/index/1
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762502460$j60$l0$h0; _gat_UA-97814751-2=1
Connection: keep-alive
```
```
GET /custom/obtenerLogoCliente HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/evento/index/1
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762502460$j60$l0$h0; _gat_UA-97814751-2=1
Connection: keep-alive
```
## 14. Recalcular (opción 1)
![alt text](imagenes/recalcular_1.png)
Entramos en la sección "Análisis de riesgos" y a continuación pulsamos el botón "Recalcular".
### ¿Qué se recibe al entrar en esta sección?
```
POST /analisisRiesgo/generarAnalisisRiesgoMin/1 HTTP/1.1
Host: 172.20.48.129:8090
Content-Length: 0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: */*
X-Requested-With: XMLHttpRequest
Origin: http://172.20.48.129:8090
Referer: http://172.20.48.129:8090/analisisRiesgo/index/1
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762502855$j60$l0$h0
Connection: keep-alive
```
```
GET /analisisRiesgo/cargarAnalisisRiesgoTabla/1?from=index&draw=2&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=false&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=6&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=7&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=&columns%5B8%5D%5Bname%5D=&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=false&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=&columns%5B9%5D%5Bname%5D=&columns%5B9%5D%5Bsearchable%5D=true&columns%5B9%5D%5Borderable%5D=false&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B10%5D%5Bdata%5D=&columns%5B10%5D%5Bname%5D=&columns%5B10%5D%5Bsearchable%5D=true&columns%5B10%5D%5Borderable%5D=false&columns%5B10%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B10%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B11%5D%5Bdata%5D=&columns%5B11%5D%5Bname%5D=&columns%5B11%5D%5Bsearchable%5D=true&columns%5B11%5D%5Borderable%5D=false&columns%5B11%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B11%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B12%5D%5Bdata%5D=&columns%5B12%5D%5Bname%5D=&columns%5B12%5D%5Bsearchable%5D=true&columns%5B12%5D%5Borderable%5D=false&columns%5B12%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B12%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B13%5D%5Bdata%5D=&columns%5B13%5D%5Bname%5D=&columns%5B13%5D%5Bsearchable%5D=true&columns%5B13%5D%5Borderable%5D=true&columns%5B13%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B13%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B14%5D%5Bdata%5D=&columns%5B14%5D%5Bname%5D=&columns%5B14%5D%5Bsearchable%5D=true&columns%5B14%5D%5Borderable%5D=true&columns%5B14%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B14%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B15%5D%5Bdata%5D=&columns%5B15%5D%5Bname%5D=&columns%5B15%5D%5Bsearchable%5D=true&columns%5B15%5D%5Borderable%5D=true&columns%5B15%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B15%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B16%5D%5Bdata%5D=&columns%5B16%5D%5Bname%5D=&columns%5B16%5D%5Bsearchable%5D=true&columns%5B16%5D%5Borderable%5D=true&columns%5B16%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B16%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B17%5D%5Bdata%5D=&columns%5B17%5D%5Bname%5D=&columns%5B17%5D%5Bsearchable%5D=true&columns%5B17%5D%5Borderable%5D=true&columns%5B17%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B17%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B18%5D%5Bdata%5D=&columns%5B18%5D%5Bname%5D=&columns%5B18%5D%5Bsearchable%5D=true&columns%5B18%5D%5Borderable%5D=true&columns%5B18%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B18%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=16&order%5B0%5D%5Bdir%5D=desc&start=0&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1762502851864 HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/analisisRiesgo/index/1
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762502855$j60$l0$h0
Connection: keep-alive
```
## 15. Recalcular (opción 2)
![alt text](imagenes/recalcular_2.png)
### ¿Qué se recibe al entrar en esta sección?
```
POST /RSA/recalculateRAjax/1?acam=false&ar=true&pdt=false&vr=6&con=true&po=true&dim=true HTTP/1.1
Host: 172.20.48.129:8090
Content-Length: 0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: */*
X-Requested-With: XMLHttpRequest
Origin: http://172.20.48.129:8090
Referer: http://172.20.48.129:8090/analisisRiesgo/index/1
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762502855$j60$l0$h0
Connection: keep-alive
```
## 16. Cerrar sesión
![alt text](imagenes/cerrar_sesion.png)
### ¿Qué se recibe al entrar en esta sección?
```
GET /logout/index HTTP/1.1
Host: 172.20.48.129:8090
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://172.20.48.129:8090/analisisRiesgo/index/1
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762502855$j60$l0$h0
Connection: keep-alive
```
```
GET /logoff HTTP/1.1
Host: 172.20.48.129:8090
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://172.20.48.129:8090/analisisRiesgo/index/1
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762502855$j60$l0$h0
Connection: keep-alive
```
```
GET / HTTP/1.1
Host: 172.20.48.129:8090
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://172.20.48.129:8090/analisisRiesgo/index/1
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; JSESSIONID=510A6D0C8E31CEAE7E9E874B51848694; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762502855$j60$l0$h0
Connection: keep-alive
```
```
GET /login/auth HTTP/1.1
Host: 172.20.48.129:8090
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://172.20.48.129:8090/analisisRiesgo/index/1
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762502855$j60$l0$h0; JSESSIONID=4FDDA0257242BFA72EB9534C9662AA43
Connection: keep-alive
```
```
GET /login/authAjax HTTP/1.1
Host: 172.20.48.129:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: */*
X-Requested-With: XMLHttpRequest
Referer: http://172.20.48.129:8090/analisisRiesgo/index/1
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.1.1791792627.1762429181; _gid=GA1.1.1977960298.1762429181; _ga_55LR48RTVX=GS2.1.s1762499598$o2$g1$t1762502855$j60$l0$h0; JSESSIONID=4FDDA0257242BFA72EB9534C9662AA43
Connection: keep-alive
```
```
GET /recaptcha/api2/anchor?ar=1&k=6LdOYd4UAAAAAJp9Z0nvTa8Y9xYqE_q6NHRSGiyq&co=aHR0cDovLzE3Mi4yMC40OC4xMjk6ODA5MA..&hl=es&v=naPR4A6FAh-yZLuCX253WaZq&size=invisible&anchor-ms=20000&execute-ms=15000&cb=5rnq8s1m7x57 HTTP/2
Host: www.google.com
Cookie: _GRECAPTCHA=09ADiQh0dbcaH8oDFGLI8hlny2zL0M4kQNYXpYA0-OuFUg-qpZhBZTsA3lf3Vl8F9w6FK_hdInM-TOauBsQe_ciP8
Sec-Ch-Ua: "Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: iframe
Sec-Fetch-Storage-Access: active
Referer: http://172.20.48.129:8090/
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Priority: u=0, i
```
```
GET /recaptcha/api2/anchor?ar=1&k=6LdOYd4UAAAAAJp9Z0nvTa8Y9xYqE_q6NHRSGiyq&co=aHR0cDovLzE3Mi4yMC40OC4xMjk6ODA5MA..&hl=es&v=naPR4A6FAh-yZLuCX253WaZq&size=invisible&anchor-ms=20000&execute-ms=15000&cb=icmhf5ec4300 HTTP/2
Host: www.google.com
Cookie: _GRECAPTCHA=09ADiQh0dbcaH8oDFGLI8hlny2zL0M4kQNYXpYA0-OuFUg-qpZhBZTsA3lf3Vl8F9w6FK_hdInM-TOauBsQe_ciP8
Sec-Ch-Ua: "Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: iframe
Sec-Fetch-Storage-Access: active
Referer: http://172.20.48.129:8090/
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Priority: u=0, i
```
```
POST /recaptcha/api2/clr?k=6LdOYd4UAAAAAJp9Z0nvTa8Y9xYqE_q6NHRSGiyq HTTP/2
Host: www.google.com
Content-Length: 124
Sec-Ch-Ua-Platform: "Windows"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
Sec-Ch-Ua: "Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Accept: */*
Origin: http://172.20.48.129:8090
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: empty
Referer: http://172.20.48.129:8090/
Accept-Encoding: gzip, deflate, br
Accept-Language: es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Priority: u=1, i


(6LdOYd4UAAAAAJp9Z0nvTa8Y9xYqE_q6NHRSGiyq
```
