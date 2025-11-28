import json
import httpx
from fastapi import FastAPI

app = FastAPI()

def load_session_cookies():
    with open("session.json", "r") as file:
        return json.load(file)
    
@app.get("/proyectos")
async def obtener_proyectos():
    cookies = load_session_cookies()

    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    print(cookie_header)

    url = "http://172.20.48.129:8090/proyecto/cargarProyectosTabla/"

    params = {
        "draw": "1",
        "columns[0][data]": "0",
        "columns[0][searchable]": "false",
        "columns[0][orderable]": "true",
        "columns[1][data]": "1",
        "columns[2][data]": "2",
        "columns[3][data]": "3",
        "columns[4][data]": "4",
        "columns[5][data]": "5",
        "columns[6][data]": "6",
        "order[0][column]": "1",
        "order[0][dir]": "asc",
        "start": "0",
        "length": "10",
        "search[value]": "",
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": cookie_header
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers, params=params)

    # Si la sesión caduca, aquí recibirás 401/403 → deberías regenerar la sesión
    r.raise_for_status()

    return r.json()