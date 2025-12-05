from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
import base64
import httpx
import urllib.parse
from . import database # Importamos el nuevo módulo de base deatos

app = FastAPI()

JSON_FIELDS = [
    "threat_id",
    "user_id",
    "activo_id", # Añadido para la consulta
    "codigo_amenaza", # Añadido para la consulta
    "device_id",
    "detected_at",
    "threat_type",
    "threat_description",
    "severity",
    "actions_taken",
    "status"
]

@app.on_event("startup")
async def startup_event():
    """Al iniciar la app, crea el pool de conexiones a la BD."""
    await database.get_db_pool()

@app.on_event("shutdown")
async def shutdown_event():
    """Al apagar la app, cierra el pool de conexiones."""
    if database.pool:
        database.pool.close()
        await database.pool.wait_closed()

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
                missing_fields.append(field)
        
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
    url_ar = config["URL_AR"]
    login_form_url = config["login_form_url"]
    existUser_url = config["existUser_url"]
    authenticate_url = config["authenticate_url"]

    password_b64 = base64.b64encode(password.encode("utf-8")).decode("utf-8")
    password_encoded = urllib.parse.quote_plus(password_b64)

    headers_existUser = {
        "Host": url_ar.replace("http://", ""),
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": url_ar,
        "Referer": f"{url_ar}/login/auth",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive"
    }

    headers_authenticate = {
        "Host": url_ar.replace("http://", ""),
        "Cache-Control": "max-age=0",
        "Origin": url_ar,
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Referer": f"{url_ar}/login/auth",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "es-ES,es;q=0.9",
        "Connection": "keep-alive"
    }

    payload = f"username={username}&password={password_encoded}"

    async with httpx.AsyncClient(follow_redirects=False) as client:

        print("---- GET LOGIN PAGE ----")
        form_response = await client.get(login_form_url)
        print("FORM STATUS:", form_response.status_code)
        print("FORM HEADERS:", form_response.headers)
        print("FORM COOKIES:", client.cookies)

        login_response = await client.post(existUser_url, content = payload, headers = headers_existUser)

        print("---- POST EXIST USER ----")
        print("RESPUESTA AL LOGIN")
        print("EXIST USER STATUS:", login_response.status_code)
        print("EXIST USER HEADERS:", login_response.headers)
        print("EXIST USER COOKIES:", client.cookies)

        login_authenticate = await client.post(authenticate_url, content = payload, headers = headers_authenticate)

        print("---- POST AUTHENTICATE ----")
        print("RESPUESTA A AUTHENTICATE")
        print("AUTH STATUS:", login_authenticate.status_code)
        print("AUTH COOKIES:", client.cookies)
        print("AUTHENTICATE:", login_authenticate.text[:200])
        print("LOC:", login_authenticate.headers)
        print("SET-COOKIE:", login_authenticate.headers.get("set-cookie"))

    return{
        "status": "login_attempted"
    }
