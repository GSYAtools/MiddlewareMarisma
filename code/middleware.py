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

    payload = {
        "username": username,
        "password": password_encoded
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(login_url, data = payload, headers = headers)

    print("RESPUESTA AL LOGIN")
    print("STATUS:", response.status_code)
    print("HEADERS:", response.headers)
    print("BODY:", response.text)

    return{
        "status": "login_attempted",
        "http_status": response.status_code,
        "response_preview": response.text[:200]
    }
