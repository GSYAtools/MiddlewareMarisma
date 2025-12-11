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

def load_session_cookie():
    with open("session.json", "r") as file:
        return json.load(file)

SESSION_COOKIES = load_session_cookie()

@app.middleware("http")
async def middleware(request: Request, call_next):
    async with httpx.AsyncClient(follow_redirects=True) as client:
        for name, value in SESSION_COOKIES.items():
            client.cookies.set(name, value, domain="172.20.48.129", path="/")

        login_authenticate_url = "http://172.20.48.129:8090/login/authenticate"
        try:
            resp = await client.get(login_authenticate_url)
            if resp.status_code != 200:
                print("GET de login no devolvió 200", resp.status_code)
        except Exception as e:
            print("Error en GET login:", e)

        request.state.client = client
        response = await call_next(request)

        return response
    

@app.get("/login")
async def login(request: Request):
    client = request.state.client

    authenticate_url = "http://172.20.48.129:8090/login/authenticate"
    response_authenticate = await client.get(authenticate_url)

    return{
        "status": response_authenticate.status_code,
        "preview": response_authenticate.text[:300]
    }

@app.get("/")
async def home(request: Request):
    client = request.state.client

    home_url = "http://172.20.48.129:8090/"
    response_home = await client.get(home_url)

    return {
        "status": response_home.status_code,
        "html_preview": response_home.text[:500]
    }

@app.get("/proyecto/obtenerMisProyectos")
async def obtener_proyectos(request: Request):
    client = request.state.client

    mis_proyectos_url = "http://172.20.48.129:8090/proyecto/obtenerMisProyectos/"

    headers = {
        "Host": "172.20.48.129:8090",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "http://172.20.48.129:8090/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "es-ES,es;q=0.9",
        "Cookie": "_ga=GA1.1.1975039891.1762334083; _gid=GA1.1.2030846257.1764155102; _ga_55LR48RTVX=GS2.1.s1764157309$o8$g1$t1764157397$j60$l0$h0; JSESSIONID={}",
        "Connection": "keep-alive"
    }

    resp = await client.get(mis_proyectos_url, headers = headers)

    try:
        data = resp.json()  # parseamos a JSON
    except Exception:
        return {"status": resp.status_code, "raw_text": resp.text[:300]}

    return {
        "status": resp.status_code, 
        "data": data
    }

@app.get("/proyecto/cargarProyectosTabla")
async def cargar_proyectos_tabla(request: Request, draw: int = 1):
    client = request.state.client
    url = f"http://172.20.48.129:8090/proyecto/cargarProyectosTabla/?draw={draw}"
    resp = await client.get(url)

    try:
        data = resp.json()
    except Exception:
        return {"status": resp.status_code, "raw_text": resp.text[:300]}

    return {"status": resp.status_code, "data": data}