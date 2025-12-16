# services/steps.py
from typing import Any, Dict, List
from client.risk_client import RiskClient
import logging

logger = logging.getLogger("services.steps")

async def step_login_exist(client: RiskClient) -> Dict[str, Any]:
    r = await client.exist_user()
    return {"step": "exist_user", "status": r.status_code, "ok": r.is_success}

async def step_authenticate(client: RiskClient) -> Dict[str, Any]:
    r = await client.authenticate()
    # Ejemplo: analizar redirección
    location = r.headers.get("Location")
    return {"step": "authenticate", "status": r.status_code, "location": location}

async def step_get_projects(client: RiskClient) -> Dict[str, Any]:
    # parámetros por defecto, puedes parametrizar desde config
    params = {
        "draw": "1",
        "start": "0",
        "length": "10",
        "search[value]": ""
    }
    r = await client.cargar_proyectos(params=params)
    r.raise_for_status()
    return {"step": "cargar_proyectos", "body": r.json()}

async def step_get_subprojects(client: RiskClient, subproject_id: int = 1) -> Dict[str, Any]:
    params = {"draw": "1", "start": "0", "length": "10", "search[value]": ""}
    r = await client.cargar_subproyectos(subproject_id, params=params)
    r.raise_for_status()
    return {"step": "cargar_subproyectos", "subproject_id": subproject_id, "body": r.json()}

# flow explícito (ordenado)
async def run_all_flow(client: RiskClient) -> List[Dict[str, Any]]:
    results = []

    # Orden explícito - añade o quita pasos según necesites
    results.append(await step_login_exist(client))
    results.append(await step_authenticate(client))
    results.append(await step_get_projects(client))
    results.append(await step_get_subprojects(client, subproject_id=1))

    # Añade más pasos mapeando las funciones anteriores
    return results
