# routes/routes.py
from fastapi import APIRouter, Depends
from client.risk_client import RiskClient
import services.emarisma_http_service as steps
from config.loader import load_config
from services.internal_db_service import save_request

router = APIRouter()

def get_client(settings = Depends(load_config)):
    return RiskClient(settings)

@router.post("/new_incident")
async def new_incident(data: dict, client: RiskClient = Depends(get_client)):
    # Primero, guardar la request en la DB interna
    request_id = await save_request(data)
    # Luego, ejecutar el flujo completo
    incident_id = await steps.run_all_flow(client, data)
    return {"request_id": request_id, "incident_id": incident_id}

@router.get("/retrive_incident/{incident_id}")
async def retrive_incident(incident_id: str, client: RiskClient = Depends(get_client)):
    return await steps.run_all_flow(client, incident_id)