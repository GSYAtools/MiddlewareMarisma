# routes/step_routes.py
from fastapi import APIRouter, Depends
from client.risk_client import RiskClient
from services import steps
from config.loader import load_config

router = APIRouter()

def get_client(settings = Depends(load_config)):
    return RiskClient(settings)

@router.post("/login/existUser")
async def exist_user_route(client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        return await steps.step_login_exist(client)
    finally:
        await client.shutdown()

@router.post("/login/authenticate")
async def authenticate_route(client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        return await steps.step_authenticate(client)
    finally:
        await client.shutdown()

@router.get("/proyectos")
async def proyectos_route(client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        return await steps.step_get_projects(client)
    finally:
        await client.shutdown()

@router.get("/subproyectos/{subproject_id}")
async def subproyectos_route(subproject_id: int = 2, client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        return await steps.step_get_subprojects(client, subproject_id=subproject_id)
    finally:
        await client.shutdown()

# --- Incidentes y eventos ---
@router.post("/evento/save")
async def guardar_incidente_route(client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        return await steps.step_guardar_incidente(client)
    finally:
        await client.shutdown()

@router.get("/eventos/{subproject_id}")
async def eventos_route(subproject_id: int = 3, client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        return await steps.step_obtener_eventos(client, subproject_id=subproject_id)
    finally:
        await client.shutdown()

@router.post("/incidente/guardarGravedad")
async def guardar_gravedad_route(client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        return await steps.step_guardar_gravedad(client)
    finally:
        await client.shutdown()

@router.post("/incidente/guardarAmenaza/{id_amenaza}")
async def guardar_amenaza_route(client: RiskClient = Depends(get_client), id_amenaza: int = 690):
    await client.startup()
    try:
        return await steps.step_guardar_amenaza(client, id_amenaza=id_amenaza)
    finally:
        await client.shutdown()

@router.get("/incidente/cargarIncidente/{incidente_id}")
async def cargar_incidente_route(client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        return await steps.step_cargar_incidente(client)
    finally:
        await client.shutdown()

# --- Controles y activos ---
@router.get("/incidente/cargarTablaControlesNoImplicados/{incidente_id}")
async def controles_no_implicados_route(client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        return await steps.step_obtener_controlesNoImplicados(client)
    finally:
        await client.shutdown()

@router.get("/incidente/cargarTablaActivosNoImplicados/{incidente_id}")
async def activos_no_implicados_route(client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        return await steps.step_obtener_activosNoImplicados(client)
    finally:
        await client.shutdown()

@router.get("/incidente/cargarTablaControlesImplicados/{incidente_id}")
async def controles_implicados_route(client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        return await steps.step_obtener_controlesImplicados(client)
    finally:
        await client.shutdown()

@router.get("/incidente/cargarTablaActivosImplicados/{incidente_id}")
async def activos_implicados_route(client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        return await steps.step_obtener_activosImplicados(client)
    finally:
        await client.shutdown()

# --- Dimensiones y vinculación ---
@router.get("/incidente/cargarDimensionesClear")
async def dimensiones_clear_route(client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        return await steps.step_cargar_dimensionesClear(client)
    finally:
        await client.shutdown()

@router.get("/incidente/vincularActivo")
async def vincular_activo_route(client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        return await steps.step_vincular_activo(client)
    finally:
        await client.shutdown()

@router.get("/incidente/vincularControl")
async def vincular_control_route(client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        return await steps.step_vincular_control(client)
    finally:
        await client.shutdown()

# --- Recalcular ---
@router.post("/recalculate")
async def recalcular_route(client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        return await steps.step_recalcular(client)
    finally:
        await client.shutdown()

# --- Flow completo ---
@router.post("/run_all")
async def run_all_route(client: RiskClient = Depends(get_client)):
    await client.startup()
    try:
        results = await steps.run_all_flow(client)
        return {"results": results}
    finally:
        await client.shutdown()
