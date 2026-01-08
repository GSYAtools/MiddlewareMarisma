# routes/routes.py
from fastapi import APIRouter, Depends
from client.risk_client import RiskClient
import services.emarisma_http_service as steps
from config.loader import load_config

router = APIRouter()

def get_client(settings = Depends(load_config)):
    return RiskClient(settings)

@router.post("/new_incident")
async def new_incident(data: dict, client: RiskClient = Depends(get_client)):
    incident_id = await steps.run_all_flow(client, data)
    return {"incident_id": incident_id}

@router.get("/retrive_incident/{incident_id}")
async def retrive_incident(incident_id: str, client: RiskClient = Depends(get_client)):
    return await steps.run_all_flow(client, incident_id)