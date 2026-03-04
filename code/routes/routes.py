# routes/routes.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from client.risk_client import RiskClient
import services.emarisma_http_service as steps
from config.loader import load_config
from services.internal_db_service import (
    save_request,
    update_request_status,
    update_request_risk_previo,
    update_request_risk_nuevo,
)
from services.emarisma_db_service import (
    get_proyecto_id_by_name,
    get_subproyecto_id_by_name,
    get_tipo_amenaza_instanciada_id_by_subproyecto_and_nombre,
    get_activo_id_by_name,
    get_amenaza_instanciada_id,
    get_activo_amenaza_id,
    get_analisis_riesgo_by_activo_amenaza_id,
)
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
    controls: Optional[str] = None  # Controles separados por ';', ej. "A.05.01;A.05.02"

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
    
    # 1. Recuperar proyecto_id y validar
    logger.info(f"Buscando ID para proyecto: {data.project_name}")
    proyecto_id = await get_proyecto_id_by_name(data.project_name)
    if proyecto_id is None:
        logger.error(f"Proyecto no encontrado: {data.project_name}")
        raise HTTPException(status_code=404, detail=f"El proyecto '{data.project_name}' no existe en la base de datos")
    logger.info(f"Proyecto ID obtenido: {proyecto_id}")
    
    # 2. Recuperar subproyecto_id y validar
    logger.info(f"Buscando ID para subproyecto: {data.subproject_name}")
    subproyecto_id = await get_subproyecto_id_by_name(data.subproject_name)
    if subproyecto_id is None:
        logger.error(f"Subproyecto no encontrado: {data.subproject_name}")
        raise HTTPException(status_code=404, detail=f"El subproyecto '{data.subproject_name}' no existe en la base de datos")
    logger.info(f"Subproyecto ID obtenido: {subproyecto_id}")
    
    # 3. Obtener activo_id y validar
    logger.info(f"Buscando activo_id para nombre: {data.device_id}")
    activo_id = await get_activo_id_by_name(data.device_id)
    if activo_id is None:
        logger.error(f"Activo no encontrado: {data.device_id}")
        raise HTTPException(status_code=404, detail=f"El activo '{data.device_id}' no existe en la base de datos")
    logger.info(f"Activo ID obtenido: {activo_id}")
    
    # 4. Validar y normalizar severity
    severity_lower = data.severity.lower()
    severity_map = {
        "leve": "leve",
        "grave": "grave",
        "low": "leve",
        "high": "grave"
    }
    if severity_lower not in severity_map:
        logger.error(f"Valor de severity inválido: {data.severity}")
        raise HTTPException(status_code=400, detail=f"El valor de severity '{data.severity}' no es válido. Valores permitidos: 'leve', 'grave', 'low', 'high'")
    severity_normalized = severity_map[severity_lower]
    logger.info(f"Severity normalizado: {severity_normalized}")
    
    # 5. Obtener amenaza_instanciada_id y validar
    logger.info(f"Buscando amenaza_instanciada_id para subproyecto: {subproyecto_id}, threat_type: {data.threat_type}")
    tipo_amenaza_id = await get_tipo_amenaza_instanciada_id_by_subproyecto_and_nombre(subproyecto_id, data.threat_type)
    if tipo_amenaza_id is None:
        logger.error(f"Amenaza instanciada no encontrada para threat_type: {data.threat_type}")
        raise HTTPException(status_code=404, detail=f"La amenaza '{data.threat_type}' no existe para el subproyecto '{data.subproject_name}'")
    logger.info(f"Amenaza instanciada ID obtenido: {tipo_amenaza_id}")
    
    # Construir JSON con datos asociados (usar severity normalizado)
    emarisma_data = {
        "proyecto_id": proyecto_id,
        "subproyecto_id": subproyecto_id,
        "tipo_amenaza_instanciada_id": tipo_amenaza_id,
        "severity": severity_normalized,
        "device_id": activo_id
    }

    # Obtener activo_amenaza_id y snapshot PREVIO de analisis_riesgo
    amenaza_instanciada_id = await get_amenaza_instanciada_id(tipo_amenaza_id, subproyecto_id)
    activo_amenaza_id = None
    analisis_previo = None

    if amenaza_instanciada_id:
        activo_amenaza_id = await get_activo_amenaza_id(amenaza_instanciada_id, activo_id)
        if activo_amenaza_id:
            analisis_previo = await get_analisis_riesgo_by_activo_amenaza_id(activo_amenaza_id)
        else:
            logger.warning(
                f"No se encontró activo_amenaza_id para amenaza_instanciada_id={amenaza_instanciada_id} y activo_id={activo_id}"
            )
    else:
        logger.warning(
            f"No se encontró amenaza_instanciada_id para tipo_amenaza_id={tipo_amenaza_id} y subproyecto_id={subproyecto_id}"
        )

    emarisma_data["activo_amenaza_id"] = activo_amenaza_id

    await update_request_risk_previo(
        request_id,
        riesgo_inherente_previo=analisis_previo["riesgo_inherente"] if analisis_previo else None,
        riesgo_previo=analisis_previo["riesgo"] if analisis_previo else None,
        valor_riesgo_previo=analisis_previo["valor_riesgo"] if analisis_previo else None,
    )
    logger.info(f"Valores previos de riesgo guardados para request_id: {request_id}")

    # Máquina de estados: pending cuando se lanza el flujo
    await update_request_status(request_id, "pending")
    logger.info(f"Estado request_id={request_id} actualizado a pending")
    
    # Ejecutar el flujo completo con el JSON de datos asociados
    logger.info("Iniciando flujo completo")
    flow_error = None
    try:
        await steps.run_all_flow(client, data_dict, emarisma_data)
        logger.info("Flujo completo terminado")
    except Exception as e:
        flow_error = e
        logger.error(f"Error durante el flujo completo: {e}")
    finally:
        if activo_amenaza_id:
            analisis_actual = await get_analisis_riesgo_by_activo_amenaza_id(activo_amenaza_id)
            if flow_error is None:
                await update_request_risk_nuevo(
                    request_id,
                    riesgo_inherente_nuevo=analisis_actual["riesgo_inherente"] if analisis_actual else None,
                    riesgo_nuevo=analisis_actual["riesgo"] if analisis_actual else None,
                    valor_riesgo_nuevo=analisis_actual["valor_riesgo"] if analisis_actual else None,
                    status="completed",
                )
                logger.info(f"Valores nuevos de riesgo guardados y estado completed para request_id: {request_id}")
            else:
                logger.warning(f"Flujo fallido para request_id={request_id}; se mantiene estado pending")

    if flow_error:
        raise flow_error

    return {"request_id": request_id}

@router.get("/retrive_incident/{incident_id}")
async def retrive_incident(incident_id: str, client: RiskClient = Depends(get_client)):
    #return await steps.run_all_flow(client, incident_id) ----- Esto tiene que ser una consulta a la SQLite -----
    return None