# routes/steps_routes.py
from fastapi import APIRouter, Depends
from client.risk_client import RiskClient
from services import steps
from config.loader import load_config

router = APIRouter()

def get_client(settings = Depends(load_config)):
    # Este dependencie devuelve un RiskClient en runtime: usamos el mismo settings para inicializar
    return RiskClient(settings)

@router.post("/login/existUser")
async def exist_user_route(client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        r = await client.exist_user()
        return {"status": r.status_code, "text": r.text}
    finally:
        await client.shutdown()

@router.post("/login/authenticate")
async def authenticate_route(client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        r = await client.authenticate()
        return {"status": r.status_code, "location": r.headers.get("Location")}
    finally:
        await client.shutdown()

@router.get("/proyectos")
async def proyectos_route(client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        r = await client.cargar_proyectos()
        r.raise_for_status()
        return r.json()
    finally:
        await client.shutdown()

@router.get("/subproyectos/{subproject_id}")
async def subproyectos_route(subproject_id: int, client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        r = await client.cargar_subproyectos(subproject_id)
        r.raise_for_status()
        return r.json()
    finally:
        await client.shutdown()

@router.post("/run_all")
async def run_all_route(client: RiskClient = Depends(get_client)):
    """
    Ejecuta todo el flujo en el orden definido en services.steps.run_all_flow
    """
    await client.startup()
    try:
        results = await steps.run_all_flow(client)
        return {"results": results}
    finally:
        await client.shutdown()
