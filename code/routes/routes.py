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
    get_request,
)
from services.emarisma_db_service import (
    get_proyecto_id_by_name,
    get_subproyecto_id_by_name,
    get_tipo_amenaza_instanciada_id_by_subproyecto_and_nombre,
    get_activo_id_by_name,
    get_activo_amenaza_id,
    get_analisis_riesgo_by_activo_amenaza_id,
    get_all_subproyectos,
    get_activos_by_subproyecto,
)
from client_instance import client
import logging
import asyncio
import time

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

async def process_incident_flow(
    request_id: int,
    client: RiskClient,
    data_dict: dict,
    emarisma_data: dict,
    activo_amenaza_id: int,
    analisis_previo: dict
):
    """
    Procesa el flujo completo de incidente en segundo plano.
    Ejecuta el flujo, espera a que cambien los valores de riesgo y actualiza la BD.
    """
    logger.info(f"Iniciando procesamiento en segundo plano para request_id={request_id}")
    flow_error = None
    
    try:
        await steps.run_all_flow(client, data_dict, emarisma_data)
        logger.info(f"Flujo completo terminado para request_id={request_id}")
    except Exception as e:
        flow_error = e
        logger.error(f"Error durante el flujo completo para request_id={request_id}: {e}")
    
    # Polling para detectar cambios en los valores de riesgo
    if activo_amenaza_id and flow_error is None:
        timeout = 120  # segundos
        poll_interval = 2  # segundos entre lecturas
        start_time = time.time()
        analisis_actual = None
        valores_cambiaron = False
        
        logger.info(f"Iniciando polling para detectar cambios en riesgo (timeout: {timeout}s) para request_id={request_id}")
        
        while time.time() - start_time < timeout:
            analisis_actual = await get_analisis_riesgo_by_activo_amenaza_id(activo_amenaza_id)
            
            # Comparar valores previos con actuales
            if analisis_previo and analisis_actual:
                if (analisis_previo.get("riesgo_inherente") != analisis_actual.get("riesgo_inherente") or
                    analisis_previo.get("riesgo") != analisis_actual.get("riesgo") or
                    analisis_previo.get("valor_riesgo") != analisis_actual.get("valor_riesgo")):
                    valores_cambiaron = True
                    elapsed = time.time() - start_time
                    logger.info(f"Valores de riesgo cambiaron después de {elapsed:.2f}s para request_id={request_id}")
                    break
            elif not analisis_previo and analisis_actual:
                # Si no había valores previos pero ahora sí hay, considerar como cambio
                valores_cambiaron = True
                logger.info(f"Valores de riesgo detectados (no existían previamente) para request_id={request_id}")
                break
            
            # Esperar antes de la siguiente lectura
            await asyncio.sleep(poll_interval)
        
        if not valores_cambiaron:
            elapsed = time.time() - start_time
            logger.warning(f"Timeout de {timeout}s alcanzado. Valores no cambiaron después de {elapsed:.2f}s para request_id={request_id}")
        
        # Guardar los valores nuevos (hayan cambiado o no)
        try:
            await update_request_risk_nuevo(
                request_id,
                riesgo_inherente_nuevo=analisis_actual.get("riesgo_inherente") if analisis_actual else None,
                riesgo_nuevo=analisis_actual.get("riesgo") if analisis_actual else None,
                valor_riesgo_nuevo=analisis_actual.get("valor_riesgo") if analisis_actual else None,
                status="completed",
            )
            logger.info(f"Valores nuevos de riesgo guardados y estado completed para request_id={request_id}")
        except Exception as e:
            logger.error(f"Error al guardar valores nuevos para request_id={request_id}: {e}")
    elif flow_error:
        logger.warning(f"Flujo fallido para request_id={request_id}; se mantiene estado pending")
    
    logger.info(f"Procesamiento en segundo plano completado para request_id={request_id}")

@router.post("/new_incident")
async def new_incident(data: IncidentRequest, client: RiskClient = Depends(get_client)):
    logger.info(f"Recibida petición new_incident: {data.dict()}")
    # Convertir a dict para guardar
    data_dict = data.dict()
    
    # === FASE 1: OBTENER TODOS LOS IDs Y CAPTURAR ANÁLISIS PREVIO (ANTES DE CUALQUIER MODIFICACIÓN) ===
    
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
    amenaza_instanciada_id = await get_tipo_amenaza_instanciada_id_by_subproyecto_and_nombre(subproyecto_id, data.threat_type)
    if amenaza_instanciada_id is None:
        logger.error(f"Amenaza instanciada no encontrada para threat_type: {data.threat_type}")
        raise HTTPException(status_code=404, detail=f"La amenaza '{data.threat_type}' no existe para el subproyecto '{data.subproject_name}'")
    logger.info(f"Amenaza instanciada ID obtenido: {amenaza_instanciada_id}")
    
    # 6. CRÍTICO: Obtener activo_amenaza_id y CAPTURAR ANÁLISIS PREVIO INMEDIATAMENTE
    logger.info("=== CAPTURANDO SNAPSHOT PREVIO DE RIESGO (ANTES DE CUALQUIER MODIFICACIÓN) ===")
    activo_amenaza_id = None
    analisis_previo = None

    if amenaza_instanciada_id:
        activo_amenaza_id = await get_activo_amenaza_id(amenaza_instanciada_id, activo_id)
        if activo_amenaza_id:
            analisis_previo = await get_analisis_riesgo_by_activo_amenaza_id(activo_amenaza_id)
            logger.info(f"Snapshot previo capturado para activo_amenaza_id={activo_amenaza_id}: {analisis_previo}")
        else:
            logger.warning(
                f"No se encontró activo_amenaza_id para amenaza_instanciada_id={amenaza_instanciada_id} y activo_id={activo_id}"
            )
    else:
        logger.warning(
            f"No se encontró amenaza_instanciada_id para amenaza_instanciada_id={amenaza_instanciada_id} y subproyecto_id={subproyecto_id}"
        )
    
    # === FASE 2: GUARDAR REQUEST Y PREPARAR DATOS ===
    
    # Ahora sí, guardar la request en la DB interna
    request_id = await save_request(data_dict)
    logger.info(f"Request guardada con ID: {request_id}")
    
    # Construir JSON con datos asociados
    emarisma_data = {
        "proyecto_id": proyecto_id,
        "subproyecto_id": subproyecto_id,
        "tipo_amenaza_instanciada_id": amenaza_instanciada_id,
        "severity": severity_normalized,
        "device_id": activo_id,
        "activo_amenaza_id": activo_amenaza_id
    }

    await update_request_risk_previo(
        request_id,
        riesgo_inherente_previo=analisis_previo.get("riesgo_inherente") if analisis_previo else None,
        riesgo_previo=analisis_previo.get("riesgo") if analisis_previo else None,
        valor_riesgo_previo=analisis_previo.get("valor_riesgo") if analisis_previo else None,
    )
    logger.info(f"Valores previos de riesgo guardados para request_id: {request_id}")

    # Máquina de estados: pending cuando se lanza el flujo
    await update_request_status(request_id, "pending")
    logger.info(f"Estado request_id={request_id} actualizado a pending")
    
    # Lanzar el procesamiento en segundo plano
    asyncio.create_task(
        process_incident_flow(
            request_id=request_id,
            client=client,
            data_dict=data_dict,
            emarisma_data=emarisma_data,
            activo_amenaza_id=activo_amenaza_id,
            analisis_previo=analisis_previo
        )
    )
    logger.info(f"Tarea en segundo plano creada para request_id={request_id}")
    
    # Devolver inmediatamente el request_id sin esperar
    return {"request_id": request_id}

@router.get("/retrive_incident/{incident_id}")
async def retrive_incident(incident_id: str, client: RiskClient = Depends(get_client)):
    """
    Retrieves the status and risk analysis of an incident by its UUID.
    
    Returns:
    - If pending: A message indicating the incident is still being processed
    - If completed: The previous and new risk analysis values
    - If not found: 404 error with message about incorrect ID
    """
    logger.info(f"Retrieving incident status: {incident_id}")
    
    request_data = await get_request(incident_id)
    if not request_data:
        logger.error(f"Incident not found: {incident_id}")
        raise HTTPException(status_code=404, detail="Incorrect incident ID. The incident does not exist.")
    
    status = request_data['status']
    logger.info(f"Incident status retrieved for {incident_id}: {status}")
    
    if status == "pending":
        return {
            "incident_id": incident_id,
            "status": "pending",
            "message": "The incident is still being processed. Please try again later."
        }
    
    elif status == "completed":
        return {
            "incident_id": incident_id,
            "status": "completed",
            "risk_analysis": {
                "previous": {
                    "riesgo_inherente": request_data['riesgo_inherente_previo'],
                    "riesgo": request_data['riesgo_previo'],
                    "valor_riesgo": request_data['valor_riesgo_previo']
                },
                "current": {
                    "riesgo_inherente": request_data['riesgo_inherente_nuevo'],
                    "riesgo": request_data['riesgo_nuevo'],
                    "valor_riesgo": request_data['valor_riesgo_nuevo']
                }
            }
        }
    
    else:
        return {
            "incident_id": incident_id,
            "status": status,
            "message": f"Incident status: {status}"
        }

@router.get("/subprojects")
async def list_subprojects():
    """
    Get the list of names of all available subprojects.
    """
    logger.info("Fetching list of subprojects")
    subprojects = await get_all_subproyectos()
    return subprojects

@router.get("/assets/{subproject_name}")
async def get_assets_by_subproject(subproject_name: str):
    """
    Get all assets (activos) belonging to a subproject by its name.
    
    Returns:
    - If subproject exists: A list of all assets with their details (id, nombre, descripcion, tipo_activo_instanciado_id)
    - If subproject not found: 404 error with message about incorrect subproject name
    """
    logger.info(f"Fetching assets for subproject: {subproject_name}")
    
    # Get subproject ID from name
    subproyecto_id = await get_subproyecto_id_by_name(subproject_name)
    if subproyecto_id is None:
        logger.error(f"Subproject not found with name: {subproject_name}")
        raise HTTPException(status_code=404, detail=f"No subproject found with name '{subproject_name}'")
    
    logger.info(f"Subproject ID obtained: {subproyecto_id}")
    
    # Get assets for the subproject
    activos = await get_activos_by_subproyecto(subproyecto_id)
    logger.info(f"Retrieved {len(activos)} assets for subproject '{subproject_name}' (ID: {subproyecto_id})")
    
    return {
        "subproject_name": subproject_name,
        "total_assets": len(activos),
        "assets": activos
    }