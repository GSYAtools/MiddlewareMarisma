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

@app.get("/subproyectos/1")
async def obtener_subproyectos():
    cookies = load_session_cookies()

    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    print(cookie_header)

    url = "http://172.20.48.129:8090/subproyecto/cargarSubproyectosTabla/1"

    params = {
        "draw": "1",

        "columns[0][data]": "",
        "columns[0][searchable]": "false",
        "columns[0][orderable]": "false",
        "columns[0][search][value]": "",
        "columns[0][search][regex]": "false",

        "columns[1][data]": "1",
        "columns[1][searchable]": "false",
        "columns[1][orderable]": "true",
        "columns[1][search][value]": "",
        "columns[1][search][regex]": "false",

        "columns[2][data]": "2",
        "columns[2][searchable]": "true",
        "columns[2][orderable]": "true",
        "columns[2][search][value]": "",
        "columns[2][search][regex]": "false",

        "columns[3][data]": "3",
        "columns[3][searchable]": "true",
        "columns[3][orderable]": "true",
        "columns[3][search][value]": "",
        "columns[3][search][regex]": "false",

        "columns[4][data]": "4",
        "columns[4][searchable]": "true",
        "columns[4][orderable]": "true",
        "columns[4][search][value]": "",
        "columns[4][search][regex]": "false",

        "columns[5][data]": "5",
        "columns[5][searchable]": "true",
        "columns[5][orderable]": "true",
        "columns[5][search][value]": "",
        "columns[5][search][regex]": "false",

        "columns[6][data]": "6",
        "columns[6][searchable]": "true",
        "columns[6][orderable]": "true",
        "columns[6][search][value]": "",
        "columns[6][search][regex]": "false",

        "columns[7][data]": "7",
        "columns[7][searchable]": "true",
        "columns[7][orderable]": "true",
        "columns[7][search][value]": "",
        "columns[7][search][regex]": "false",

        "columns[8][data]": "8",
        "columns[8][searchable]": "true",
        "columns[8][orderable]": "true",
        "columns[8][search][value]": "",
        "columns[8][search][regex]": "false",

        "order[0][column]": "1",
        "order[0][dir]": "asc",

        "start": "0",
        "length": "10",

        "search[value]": "",
        "search[regex]": "false"
    }



    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": cookie_header
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers, params=params)

    r.raise_for_status()

    return r.json()

@app.post("/evento/save")
async def guardar_incidente():
    cookies = load_session_cookies()

    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    print(cookie_header)

    url = "http://172.20.48.129:8090/evento/save"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Cookie": cookie_header
    }

    content = f"update=Guardar&id=&version=&subproyecto=1&tipo=detalle&typeAction=nuevo&responsable=Responsable4&date=05%2F12%2F2025&causa=Causa4&descripcion=Descripcion4"

    async with httpx.AsyncClient() as client:
        r = await client.post(url, headers=headers, content=content)
        print("Redireccion:", r.headers.get("Location"))

    return {"status": "login_attempted"}

@app.get("/eventos/1")
async def obtener_eventos():
    cookies = load_session_cookies()

    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    print(cookie_header)

    url = "http://172.20.48.129:8090/evento/cargarEventoTabla/1"

    params = {
        "draw": "1",

        "columns[0][data]": "0",
        "columns[0][name]": "",
        "columns[0][searchable]": "false",
        "columns[0][orderable]": "true",
        "columns[0][search][value]": "",
        "columns[0][search][regex]": "false",

        "columns[1][data]": "1",
        "columns[1][name]": "",
        "columns[1][searchable]": "true",
        "columns[1][orderable]": "true",
        "columns[1][search][value]": "",
        "columns[1][search][regex]": "false",

        "columns[2][data]": "2",
        "columns[2][name]": "",
        "columns[2][searchable]": "true",
        "columns[2][orderable]": "true",
        "columns[2][search][value]": "",
        "columns[2][search][regex]": "false",

        "columns[3][data]": "3",
        "columns[3][name]": "",
        "columns[3][searchable]": "true",
        "columns[3][orderable]": "true",
        "columns[3][search][value]": "",
        "columns[3][search][regex]": "false",

        "columns[4][data]": "4",
        "columns[4][name]": "",
        "columns[4][searchable]": "true",
        "columns[4][orderable]": "true",
        "columns[4][search][value]": "",
        "columns[4][search][regex]": "false",

        "columns[5][data]": "5",
        "columns[5][name]": "",
        "columns[5][searchable]": "true",
        "columns[5][orderable]": "true",
        "columns[5][search][value]": "",
        "columns[5][search][regex]": "false",

        "columns[6][data]": "6",
        "columns[6][name]": "",
        "columns[6][searchable]": "true",
        "columns[6][orderable]": "true",
        "columns[6][search][value]": "",
        "columns[6][search][regex]": "false",

        "columns[7][data]": "7",
        "columns[7][name]": "",
        "columns[7][searchable]": "true",
        "columns[7][orderable]": "true",
        "columns[7][search][value]": "",
        "columns[7][search][regex]": "false",

        "columns[8][data]": "",
        "columns[8][name]": "",
        "columns[8][searchable]": "true",
        "columns[8][orderable]": "false",
        "columns[8][search][value]": "",
        "columns[8][search][regex]": "false",

        "order[0][column]": "1",
        "order[0][dir]": "asc",

        "start": "0",
        "length": "10",

        "search[value]": "",
        "search[regex]": "false",
    }




    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": cookie_header
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers, params=params)

    r.raise_for_status()

    return r.json()

@app.post("/incidente/guardarGravedad")
async def guardar_gravedad():
    cookies = load_session_cookies()

    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    print(cookie_header)

    url = "http://172.20.48.129:8090/incidente/guardarGravedad"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Cookie": cookie_header
    }

    content = f"gravedad=Grave&incidente=3&subproyecto=1"

    async with httpx.AsyncClient() as client:
        r = await client.post(url, headers=headers, content=content)
    
    r.raise_for_status()

    return r.json()

@app.post("/incidente/guardarAmenaza/169")
async def guardar_amenaza():
    cookies = load_session_cookies()

    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    print(cookie_header)

    url = "http://172.20.48.129:8090/incidente/guardarAmenaza/169"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "*/*",
        "Cookie": cookie_header
    }

    content = f"gravedad=leve&evento=16"

    async with httpx.AsyncClient() as client:
        r = await client.post(url, headers=headers, content=content)
    
    r.raise_for_status()

    return r.json()

@app.get("/incidente/cargarIncidente/12")
async def cargar_incidente():
    cookies = load_session_cookies()

    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    print(cookie_header)

    url = "http://172.20.48.129:8090/incidente/cargarIncidente/12"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": cookie_header
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers)

    r.raise_for_status()

    return r.json()

@app.get("/incidente/cargarTablaControlesNoImplicados/1")
async def obtener_controlesNoImplicados():
    cookies = load_session_cookies()

    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    print(cookie_header)

    url = "http://172.20.48.129:8090/incidente/cargarTablaControlesNoImplicados/1"

    params = {
        "incidente": "12",
        "draw": "2",

        "columns[0][data]": "0",
        "columns[0][name]": "",
        "columns[0][searchable]": "false",
        "columns[0][orderable]": "true",
        "columns[0][search][value]": "",
        "columns[0][search][regex]": "false",

        "columns[1][data]": "",
        "columns[1][name]": "",
        "columns[1][searchable]": "true",
        "columns[1][orderable]": "true",
        "columns[1][search][value]": "",
        "columns[1][search][regex]": "false",

        "columns[2][data]": "",
        "columns[2][name]": "",
        "columns[2][searchable]": "true",
        "columns[2][orderable]": "true",
        "columns[2][search][value]": "",
        "columns[2][search][regex]": "false",

        "columns[3][data]": "",
        "columns[3][name]": "",
        "columns[3][searchable]": "true",
        "columns[3][orderable]": "true",
        "columns[3][search][value]": "",
        "columns[3][search][regex]": "false",

        "columns[4][data]": "",
        "columns[4][name]": "",
        "columns[4][searchable]": "false",
        "columns[4][orderable]": "false",
        "columns[4][search][value]": "",
        "columns[4][search][regex]": "false",

        "columns[5][data]": "",
        "columns[5][name]": "",
        "columns[5][searchable]": "true",
        "columns[5][orderable]": "false",
        "columns[5][search][value]": "",
        "columns[5][search][regex]": "false",

        "columns[6][data]": "6",
        "columns[6][name]": "",
        "columns[6][searchable]": "true",
        "columns[6][orderable]": "true",
        "columns[6][search][value]": "",
        "columns[6][search][regex]": "false",

        "order[0][column]": "1",
        "order[0][dir]": "asc",

        "start": "0",
        "length": "-1",

        "search[value]": "",
        "search[regex]": "false",

        "_": 1764588130734
    }




    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": cookie_header
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers, params=params)

    r.raise_for_status()

    return r.json()

@app.get("/incidente/cargarTablaActivosNoImplicados/1")
async def obtener_activosNoImplicados():
    cookies = load_session_cookies()

    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    print(cookie_header)

    url = "http://172.20.48.129:8090/incidente/cargarTablaActivosNoImplicados/1"

    params = {
        "incidente": "12",
        "draw": "2",

        "columns[0][data]": "0",
        "columns[0][name]": "",
        "columns[0][searchable]": "false",
        "columns[0][orderable]": "true",
        "columns[0][search][value]": "",
        "columns[0][search][regex]": "false",

        "columns[1][data]": "",
        "columns[1][name]": "",
        "columns[1][searchable]": "true",
        "columns[1][orderable]": "true",
        "columns[1][search][value]": "",
        "columns[1][search][regex]": "false",

        "columns[2][data]": "",
        "columns[2][name]": "",
        "columns[2][searchable]": "true",
        "columns[2][orderable]": "true",
        "columns[2][search][value]": "",
        "columns[2][search][regex]": "false",

        "columns[3][data]": "",
        "columns[3][name]": "",
        "columns[3][searchable]": "true",
        "columns[3][orderable]": "true",
        "columns[3][search][value]": "",
        "columns[3][search][regex]": "false",

        "columns[4][data]": "4",
        "columns[4][name]": "",
        "columns[4][searchable]": "false",
        "columns[4][orderable]": "true",
        "columns[4][search][value]": "",
        "columns[4][search][regex]": "false",

        "columns[5][data]": "5",
        "columns[5][name]": "",
        "columns[5][searchable]": "false",
        "columns[5][orderable]": "true",
        "columns[5][search][value]": "",
        "columns[5][search][regex]": "false",

        "columns[6][data]": "",
        "columns[6][name]": "",
        "columns[6][searchable]": "true",
        "columns[6][orderable]": "true",
        "columns[6][search][value]": "",
        "columns[6][search][regex]": "false",

        "columns[7][data]": "",
        "columns[7][name]": "",
        "columns[7][searchable]": "true",
        "columns[7][orderable]": "true",
        "columns[7][search][value]": "",
        "columns[7][search][regex]": "false",

        "columns[8][data]": "",
        "columns[8][name]": "",
        "columns[8][searchable]": "true",
        "columns[8][orderable]": "true",
        "columns[8][search][value]": "",
        "columns[8][search][regex]": "false",

        "columns[9][data]": "9",
        "columns[9][name]": "",
        "columns[9][searchable]": "false",
        "columns[9][orderable]": "true",
        "columns[9][search][value]": "",
        "columns[9][search][regex]": "false",

        "columns[10][data]": "",
        "columns[10][name]": "",
        "columns[10][searchable]": "true",
        "columns[10][orderable]": "false",
        "columns[10][search][value]": "",
        "columns[10][search][regex]": "false",

        "order[0][column]": "2",
        "order[0][dir]": "asc",

        "start": "0",
        "length": "-1",

        "search[value]": "",
        "search[regex]": "false",

        "_": "1764588130735"
    }


    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": cookie_header
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers, params=params)

    r.raise_for_status()

    return r.json()

@app.get("/incidente/cargarTablaControlesImplicados/1")
async def obtener_controlesImplicados():
    cookies = load_session_cookies()

    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    print(cookie_header)

    url = "http://172.20.48.129:8090/incidente/cargarTablaControlesImplicados/1"

    params = {
        "incidente": "12",
        "draw": "2",
        "columns[0][data]": "0",
        "columns[0][name]": "",
        "columns[0][searchable]": "false",
        "columns[0][orderable]": "true",
        "columns[0][search][value]": "",
        "columns[0][search][regex]": "false",

        "columns[1][data]": "",
        "columns[1][name]": "",
        "columns[1][searchable]": "true",
        "columns[1][orderable]": "true",
        "columns[1][search][value]": "",
        "columns[1][search][regex]": "false",

        "columns[2][data]": "",
        "columns[2][name]": "",
        "columns[2][searchable]": "true",
        "columns[2][orderable]": "true",
        "columns[2][search][value]": "",
        "columns[2][search][regex]": "false",

        "columns[3][data]": "",
        "columns[3][name]": "",
        "columns[3][searchable]": "true",
        "columns[3][orderable]": "true",
        "columns[3][search][value]": "",
        "columns[3][search][regex]": "false",

        "columns[4][data]": "4",
        "columns[4][name]": "",
        "columns[4][searchable]": "false",
        "columns[4][orderable]": "true",
        "columns[4][search][value]": "",
        "columns[4][search][regex]": "false",

        "columns[5][data]": "5",
        "columns[5][name]": "",
        "columns[5][searchable]": "false",
        "columns[5][orderable]": "true",
        "columns[5][search][value]": "",
        "columns[5][search][regex]": "false",

        "columns[6][data]": "",
        "columns[6][name]": "",
        "columns[6][searchable]": "true",
        "columns[6][orderable]": "true",
        "columns[6][search][value]": "",
        "columns[6][search][regex]": "false",

        "columns[7][data]": "",
        "columns[7][name]": "",
        "columns[7][searchable]": "true",
        "columns[7][orderable]": "true",
        "columns[7][search][value]": "",
        "columns[7][search][regex]": "false",

        "columns[8][data]": "",
        "columns[8][name]": "",
        "columns[8][searchable]": "true",
        "columns[8][orderable]": "true",
        "columns[8][search][value]": "",
        "columns[8][search][regex]": "false",

        "columns[9][data]": "9",
        "columns[9][name]": "",
        "columns[9][searchable]": "false",
        "columns[9][orderable]": "true",
        "columns[9][search][value]": "",
        "columns[9][search][regex]": "false",

        "columns[10][data]": "",
        "columns[10][name]": "",
        "columns[10][searchable]": "true",
        "columns[10][orderable]": "false",
        "columns[10][search][value]": "",
        "columns[10][search][regex]": "false",

        "order[0][column]": "2",
        "order[0][dir]": "asc",
        "start": "0",
        "length": "-1",
        "search[value]": "",
        "search[regex]": "false",
        "_": "1764588130735"
    }



    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": cookie_header
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers, params=params)

    r.raise_for_status()

    return r.json()

@app.get("/incidente/cargarTablaActivosImplicados/1")
async def obtener_activosImplicados():
    cookies = load_session_cookies()

    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    print(cookie_header)

    url = "http://172.20.48.129:8090/incidente/cargarTablaActivosImplicados/1"

    params = {
        "incidente": "12",
        "draw": "2",
        "columns[0][data]": "0",
        "columns[0][name]": "",
        "columns[0][searchable]": "false",
        "columns[0][orderable]": "true",
        "columns[0][search][value]": "",
        "columns[0][search][regex]": "false",

        "columns[1][data]": "",
        "columns[1][name]": "",
        "columns[1][searchable]": "true",
        "columns[1][orderable]": "true",
        "columns[1][search][value]": "",
        "columns[1][search][regex]": "false",

        "columns[2][data]": "",
        "columns[2][name]": "",
        "columns[2][searchable]": "true",
        "columns[2][orderable]": "true",
        "columns[2][search][value]": "",
        "columns[2][search][regex]": "false",

        "columns[3][data]": "",
        "columns[3][name]": "",
        "columns[3][searchable]": "true",
        "columns[3][orderable]": "false",
        "columns[3][search][value]": "",
        "columns[3][search][regex]": "false",

        "columns[4][data]": "",
        "columns[4][name]": "",
        "columns[4][searchable]": "true",
        "columns[4][orderable]": "false",
        "columns[4][search][value]": "",
        "columns[4][search][regex]": "false",

        "columns[5][data]": "",
        "columns[5][name]": "",
        "columns[5][searchable]": "true",
        "columns[5][orderable]": "false",
        "columns[5][search][value]": "",
        "columns[5][search][regex]": "false",

        "order[0][column]": "2",
        "order[0][dir]": "asc",
        "start": "0",
        "length": "-1",
        "search[value]": "",
        "search[regex]": "false",
        "_": "1764588130737"
    }


    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": cookie_header
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers, params=params)

    r.raise_for_status()

    return r.json()

@app.get("/incidente/cargarDimensionesClear")
async def cargar_dimensionesClear():
    cookies = load_session_cookies()

    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    print(cookie_header)

    url = "http://172.20.48.129:8090/incidente/cargarDimensionesClear?activo=1&incidente=12"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": cookie_header
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers)

    r.raise_for_status()

    return r.json()

@app.get("/incidente/vincularActivo")
async def vincular_activo():
    cookies = load_session_cookies()

    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    print(cookie_header)

    url = "http://172.20.48.129:8090/incidente/vincularActivo?dimension=19&activo=&incidente=12&porcentaje=16&vincular=true&activoAux=1"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": cookie_header
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers)

    r.raise_for_status()

    return r.json()

@app.get("/incidente/vincularControl")
async def vincular_control():
    cookies = load_session_cookies()

    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    print(cookie_header)

    url = "http://172.20.48.129:8090/incidente/vincularControl?control=55&incidente=12"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": cookie_header
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers)

    r.raise_for_status()

    return r.json()

'''@app.get("/evento/conclusion")
async def ir_a_conclusion():
    cookies = load_session_cookies()

    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    print(cookie_header)

    url = "http://172.20.48.129:8090/evento/conclusion/15"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Cookie": cookie_header
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers)

    r.raise_for_status()

    return r.json()'''

'''@app.post("/evento/save/15")
async def guardar_y_cerrar():
    cookies = load_session_cookies()

    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    print(cookie_header)

    url = "http://172.20.48.129:8090/evento/save/15"

    data = {
        "save": "Guardar",
        "id": "15",
        "version": "3",
        "subproyecto": "1",
        "tipo": "conclusion",
        "cerrar": "true",
        "coste": "11.00€",
        "myCurrency": "EUR",
        "solucion": "Solución3",
        "conclusion": "Conclusión3",
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Cookie": cookie_header
    }

    async with httpx.AsyncClient() as client:
        r = await client.post(url, headers=headers, data=data)

    r.raise_for_status()

    return r.json()'''

@app.post("/recalculate")
async def recalcular():
    cookies = load_session_cookies()

    cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    print(cookie_header)

    url = "http://172.20.48.129:8090/RSA/recalculateRAjax/1?acam=false&ar=true&pdt=false&vr=6&con=true&po=true&dim=true"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "*/*",
        "Cookie": cookie_header
    }

    async with httpx.AsyncClient() as client:
        r = await client.post(url, headers=headers)

    r.raise_for_status()

    return r.json()