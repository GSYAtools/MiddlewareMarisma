# routes/routes.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from client.risk_client import RiskClient
import services.emarisma_http_service as steps
from config.loader import load_config
from services.internal_db_service import save_request, update_emarisma_data
from services.emarisma_db_service import get_proyecto_id_by_name, get_subproyecto_id_by_name, get_tipo_amenaza_instanciada_id_by_subproyecto_and_nombre
from client_instance import client
import logging

logger = logging.getLogger(__name__)

class IncidentRequest(BaseModel):
    threat_id: str
    user_id: str
    device_id: str
    detected_at: str  # Formato ISO, ej. "2024-10-14T12:37:00Z"
    threat_type: str
    threat_description: str
    severity: str
    actions_taken: str
    status: str
    project_name: str
    subproject_name: str
    cause: str

    """
    Ejemplo de JSON para la petición:
    {
      "threat_id": "T123456",
      "user_id": "user123",
      "device_id": "deviceABC",
      "detected_at": "2024-10-14T12:37:00Z",
      "threat_type": "Alteración de secuencia",
      "threat_description": "Description of the DDoS",
      "severity": "high",
      "actions_taken": "Access revoked, device quarantined",
      "status": "mitigated"
    }
    Nota: user_id se usa como responsable, detected_at se convierte a dd/MM/yyyy para date, threat_description para descripcion, threat_type para nombre de amenaza.
    """

router = APIRouter()

def get_client():
    return client

@router.post("/new_incident")
async def new_incident(data: IncidentRequest, client: RiskClient = Depends(get_client)):
    logger.info(f"Recibida petición new_incident: {data.dict()}")
    # Convertir a dict para guardar
    data_dict = data.dict()
    # Primero, guardar la request en la DB interna
    request_id = await save_request(data_dict)
    logger.info(f"Request guardada con ID: {request_id}")
    
    # Recuperar IDs por nombre desde la petición
    logger.info(f"Buscando IDs para proyecto: {data.project_name}, subproyecto: {data.subproject_name}")
    proyecto_id = await get_proyecto_id_by_name(data.project_name)
    subproyecto_id = await get_subproyecto_id_by_name(data.subproject_name)
    logger.info(f"IDs obtenidos - Proyecto: {proyecto_id}, Subproyecto: {subproyecto_id}")
    
    # Obtener tipo_amenaza_instanciada_id por subproyecto y nombre de amenaza (threat_type)
    logger.info(f"Buscando tipo_amenaza_instanciada_id para subproyecto: {subproyecto_id}, threat_type: {data.threat_type}")
    tipo_amenaza_id = await get_tipo_amenaza_instanciada_id_by_subproyecto_and_nombre(subproyecto_id, data.threat_type)
    logger.info(f"tipo_amenaza_instanciada_id obtenido: {tipo_amenaza_id}")
    
    # Construir JSON con datos asociados
    emarisma_data = {
        "proyecto_id": proyecto_id,
        "subproyecto_id": subproyecto_id,
        "tipo_amenaza_instanciada_id": tipo_amenaza_id
    }
    await update_emarisma_data(request_id, emarisma_data)
    logger.info(f"Datos emarisma actualizados para request_id: {request_id}")
    
    # Ejecutar el flujo completo con el JSON de datos asociados
    logger.info("Iniciando flujo completo")
    await steps.run_all_flow(client, data_dict, emarisma_data)
    logger.info("Flujo completo terminado")
    return {"request_id": request_id}

@router.get("/retrive_incident/{incident_id}")
async def retrive_incident(incident_id: str, client: RiskClient = Depends(get_client)):
    return await steps.run_all_flow(client, incident_id)