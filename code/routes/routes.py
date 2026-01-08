# routes/routes.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from client.risk_client import RiskClient
import services.emarisma_http_service as steps
from config.loader import load_config
from services.internal_db_service import save_request, update_emarisma_data
from services.emarisma_db_service import get_proyecto_id_by_name, get_subproyecto_id_by_name

class IncidentRequest(BaseModel):
    threat_id: str
    user_id: str
    device_id: str
    detected_at: str
    threat_type: str
    threat_description: str
    severity: str
    actions_taken: str
    status: str

router = APIRouter()

def get_client(settings = Depends(load_config)):
    return RiskClient(settings)

@router.post("/new_incident")
async def new_incident(data: IncidentRequest, client: RiskClient = Depends(get_client)):
    # Convertir a dict para guardar
    data_dict = data.dict()
    # Primero, guardar la request en la DB interna
    request_id = await save_request(data_dict)
    
    # Recuperar IDs por nombre desde config
    settings = load_config()
    proyecto_id = await get_proyecto_id_by_name(settings.proyecto_name)
    subproyecto_id = await get_subproyecto_id_by_name(settings.subproyecto_name)
    
    # Guardar IDs como datos asociados en DB interna
    emarisma_data = {
        "proyecto_id": proyecto_id,
        "subproyecto_id": subproyecto_id
    }
    await update_emarisma_data(request_id, emarisma_data)
    
    # Ejecutar el flujo completo con los IDs
    incident_id = await steps.run_all_flow(client, data_dict, proyecto_id, subproyecto_id)
    return {"request_id": request_id, "incident_id": incident_id}

@router.get("/retrive_incident/{incident_id}")
async def retrive_incident(incident_id: str, client: RiskClient = Depends(get_client)):
    return await steps.run_all_flow(client, incident_id)