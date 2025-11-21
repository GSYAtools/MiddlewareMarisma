from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
import base64
import httpx
import urllib.parse

app = FastAPI()

JSON_FIELDS = [
    "threat_id",
    "user_id",
    "device_id",
    "detected_at",
    "threat_type",
    "threat_description",
    "severity",
    "actions_taken",
    "status"
]

@app.middleware("http")
async def middleware(request: Request, call_next):
    if request.url.path == "/login":
        return await call_next(request)
    
    if request.method == "POST":
        body = await request.body()

        if not body.strip():
            return JSONResponse({"error": "Se esperaba JSON en el body de la petición"}, status_code = 400)
        
        try:
            data = json.loads(body.decode("utf-8"))
        except json.JSONDecodeError:
            return JSONResponse({"error": "Formato JSON inválido"}, status_code = 400)
        
        missing_fields = []

        for field in JSON_FIELDS:
            if field not in data:
                missing_fields.apend(field)
        
        if missing_fields:
            return JSONResponse({"error": "Faltan campos obligatorios", "missing_fields": missing_fields}, status_code = 400)
        
        request.state.threat_data = data

        request = Request(request.scope, receive=lambda: {"body": body})

    return await call_next(request)

@app.post("/login")
async def login():
    with open("config.json", "r") as file:
        config = json.load(file)
    
    username = config["username"]
    password = config["password"]
    login_url = config["login_url"]

    password_b64 = base64.b64encode(password.encode("utf-8")).decode("utf-8")
    password_encoded = urllib.parse.quote_plus(password_b64)

    headers = {
        "Host": "172.20.48.129:8090",
        "Content-Length": "44",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://172.20.48.129:8090",
        "Referer": "http://172.20.48.129:8090/login/auth",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive"
    }

    payload = f"username={username}&password={password_encoded}"

    async with httpx.AsyncClient() as client:
        response = await client.post(login_url, content = payload, headers = headers)

    print("RESPUESTA AL LOGIN")
    print("STATUS:", response.status_code)
    print("HEADERS:", response.headers)
    print("BODY:", response.text)

    return{
        "status": "login_attempted",
        "http_status": response.status_code,
        "response_preview": response.text[:200]
    }

'''
POST /login/authenticate HTTP/1.1
Host: 172.20.48.129:8090
Content-Length: 876
Cache-Control: max-age=0
Origin: http://172.20.48.129:8090
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://172.20.48.129:8090/login/auth
Accept-Encoding: gzip, deflate, br
Accept-Language: es-ES,es;q=0.9
Cookie: _ga=GA1.1.1975039891.1762334083; _gid=GA1.1.183082415.1763726910; _gat_UA-97814751-2=1; _gat_gtag_UA_97814751_2=1; JSESSIONID=4346CC0878E27DD35EC288DEF85F112A; _ga_55LR48RTVX=GS2.1.s1763726922$o5$g1$t1763727059$j31$l0$h0
Connection: keep-alive

username=Con_premium&password=S5%24e35bn&g-recaptcha-response=0cAFcWeA4FqECw0pU3Q9CIETkmoGVYUvdq1ntokTyGo9HAdXHeujYaFXT6OFtYwB6fIm6ZE_fGDHR4jJMZ1vB5q6SW6v_Fk5U6eMp4TC2h4PKPGWjd5BibjyL9H0JQw2M7d0SfkHKo25gZWkf-Zre1QkZJRRzdI77f5tPL_5IDvmktB-3oPJ--aaWdaf5Rc6G_EvMvMnfJp_rf12Eh3iCjTW6kKRvBEjiMwo8j6hYoqp0Lnu7PU1i5XkuFe87ngpo5trwRNu7UsJRTeoaHPXkSm1gRpbUvXyaALH34x0VsZtXXb0fMeRPWMCmUGDhE7XQnJRuQgUf4XJRBxn1kGG52YSVvXERY-zpYbrD8o0vmZrHPoJ6Lzoi77UQY-ih3lhFO7-1JQ2iJ_o40nfDQ9I3EIPaiAP2M3EaY_MYPMYBksKqulZF7BP4jnHGX5V80tOeidSMYFHrRIfFpMlM-XdGcUAFqEaksLtmppY2cxdFhWY_2BLoyNRcmaLMqVv2DL-Sx0L8Q3HKQf6XLDv2C5tTlNpTox44eWM6ZdNTHjscVBIlPtre7SV9nRVvZ47LrVzVJBWkkU_S_1nRCpbB473po3J5xTy9u7E7UamfmaGwQp-ZMOFeB_fHUo8U1qwyn5GvDJ_yj3MsQ24EeLaQQGuZdZz_PUo22PDlnAWKXdTio7DsPaJwZh49h0ozg7x9zWm_fQdWcvUuzkGWK2C8Veuzev1BHoNMlMYAhLUTvXcfOfsL07sRyt3O7C7vkF5jaJVnPkmQ8oURBzdD8&postUrl=%2Flogin%2Fauthenticate'''

