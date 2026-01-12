# services/emarisma_http_service.py
from typing import Any, Dict, List
from client.risk_client import RiskClient
import logging
from config.loader import load_config
import urllib.parse
from services.emarisma_db_service import get_subproyecto_id_by_name, get_incidente_id_by_subproyecto_and_tipo_amenaza
from datetime import datetime
import asyncio

logger = logging.getLogger("services.steps")

# --- Steps individuales ---

async def step_login_exist(client: RiskClient) -> Dict[str, Any]:
    r = await client.exist_user()
    return {"step": "exist_user", "status": r.status_code, "ok": getattr(r, "is_success", True)}

async def step_authenticate(client: RiskClient) -> Dict[str, Any]:
    r = await client.authenticate()
    location = r.headers.get("Location")
    return {"step": "authenticate", "status": r.status_code, "location": location}

async def step_get_projects(client: RiskClient) -> Dict[str, Any]:
    params = {
        "draw": "1",
        "start": "0",
        "length": "10",
        "search[value]": ""
    }
    r = await client.cargar_proyectos(params=params)
    r.raise_for_status()
    return {"step": "cargar_proyectos", "body": r.json()}

async def step_get_subprojects(client: RiskClient, subproject_id: int) -> Dict[str, Any]:
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
    r = await client.cargar_subproyectos(subproject_id, params=params)
    r.raise_for_status()
    return {"step": "cargar_subproyectos", "subproject_id": subproject_id, "body": r.json()}

async def step_guardar_incidente(client: RiskClient, data: Dict[str, Any], emarisma_data: Dict[str, Any]) -> Dict[str, Any]:
    settings = load_config()
    
    # Convertir detected_at a dd/MM/yyyy
    detected_at_dt = datetime.fromisoformat(data['detected_at'].replace('Z', '+00:00'))
    date_str = detected_at_dt.strftime('%d/%m/%Y')
    
    # Construir event_data dinámicamente
    event_data = {
        "subproyecto": str(emarisma_data['subproyecto_id']),
        "tipo": settings.new_event['tipo'],
        "typeAction": settings.new_event['typeAction'],
        "responsable": data['user_id'],
        "date": date_str,
        "causa": data['cause'],
        "descripcion": data['threat_description']
    }

    content = "&".join([f"{k}={urllib.parse.quote_plus(str(v))}" for k, v in event_data.items()])
    content = "update=Guardar&id=&version=&" + content

    r = await client.guardar_evento(content=content)
    return {"step": "guardar_incidente", "status": getattr(r, "status_code", 200)}

async def step_obtener_eventos(client: RiskClient, subproject_id: int) -> Dict[str, Any]:
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
    
    r = await client.obtener_eventos(subproject_id, params=params)
    return {"step": "obtener_eventos", "status_code": r.status_code,
        "headers": dict(r.headers),
        "body": r.json() if r.headers.get("content-type", "").startswith("application/json") else r.text
    }

async def step_guardar_gravedad(client: RiskClient, data_dict: Dict[str, Any], emarisma_data: Dict[str, Any]) -> Dict[str, Any]:
    settings = load_config()
    gravedad = data_dict['severity']  # Usar severity del request

    # Construir data usando settings pero con gravedad dinámica
    data = {
        "gravedad": gravedad,
        "incidente": str(emarisma_data['incidente_id']),
        "subproyecto": str(emarisma_data['subproyecto_id'])
    }

    if not data:
        raise ValueError("No se han encontrado datos de gravedad")

    content = "&".join([f"{k}={urllib.parse.quote_plus(str(v))}" for k, v in data.items()])

    r = await client.guardar_gravedad(content=content)
    return {"step": "guardar_gravedad", "status": getattr(r, "status_code", 200)}

async def step_guardar_amenaza(client: RiskClient, emarisma_data: Dict[str, Any]) -> Dict[str, Any]:
    data = {
        "gravedad": emarisma_data['severity'],
        "evento": str(emarisma_data['evento_id'])
    }
    id_amenaza = emarisma_data['tipo_amenaza_instanciada_id']

    if not data:
        raise ValueError("No se han encontrado datos de evento")

    content = "&".join([f"{k}={urllib.parse.quote_plus(str(v))}" for k, v in data.items()])

    r = await client.guardar_amenaza(id_amenaza, content=content)
    # No raise for status, as 302 is expected
    location = r.headers.get("Location")
    return {"step": "guardar_amenaza", "status": r.status_code, "location": location}

async def step_cargar_incidente(client: RiskClient, incidente_id: int) -> Dict[str, Any]:
    r = await client.cargar_incidente(incidente_id)
    r.raise_for_status()
    return {"step": "cargar_incidente", "body": r.json()}

async def step_obtener_controlesNoImplicados(client: RiskClient, incidente_id: int) -> Dict[str, Any]:
    params = {
        "incidente": str(incidente_id),
        "draw": "2",
        "columns[0][data]": "0", "columns[0][name]": "", "columns[0][searchable]": "false", "columns[0][orderable]": "true", "columns[0][search][value]": "", "columns[0][search][regex]": "false",
        "columns[1][data]": "", "columns[1][name]": "", "columns[1][searchable]": "true", "columns[1][orderable]": "true", "columns[1][search][value]": "", "columns[1][search][regex]": "false",
        "columns[2][data]": "", "columns[2][name]": "", "columns[2][searchable]": "true", "columns[2][orderable]": "true", "columns[2][search][value]": "", "columns[2][search][regex]": "false",
        "columns[3][data]": "", "columns[3][name]": "", "columns[3][searchable]": "true", "columns[3][orderable]": "true", "columns[3][search][value]": "", "columns[3][search][regex]": "false",
        "columns[4][data]": "", "columns[4][name]": "", "columns[4][searchable]": "false", "columns[4][orderable]": "false", "columns[4][search][value]": "", "columns[4][search][regex]": "false",
        "columns[5][data]": "", "columns[5][name]": "", "columns[5][searchable]": "true", "columns[5][orderable]": "false", "columns[5][search][value]": "", "columns[5][search][regex]": "false",
        "columns[6][data]": "6", "columns[6][name]": "", "columns[6][searchable]": "true", "columns[6][orderable]": "true", "columns[6][search][value]": "", "columns[6][search][regex]": "false",
        "order[0][column]": "1",
        "order[0][dir]": "asc",
        "start": "0",
        "length": "-1",
        "search[value]": "",
        "search[regex]": "false",
        "_": "1764588130734"
    }
    r = await client.obtener_controlesNoImplicados(params)
    r.raise_for_status()
    return {"step": "controles_no_implicados", "body": r.json()}

async def step_obtener_activosNoImplicados(client: RiskClient, incidente_id: int) -> Dict[str, Any]:
    params = {
        "incidente": str(incidente_id),
        "draw": "2",
        "columns[0][data]": "0", "columns[0][name]": "", "columns[0][searchable]": "false", "columns[0][orderable]": "true", "columns[0][search][value]": "", "columns[0][search][regex]": "false",
        "columns[1][data]": "", "columns[1][name]": "", "columns[1][searchable]": "true", "columns[1][orderable]": "true", "columns[1][search][value]": "", "columns[1][search][regex]": "false",
        "columns[2][data]": "", "columns[2][name]": "", "columns[2][searchable]": "true", "columns[2][orderable]": "true", "columns[2][search][value]": "", "columns[2][search][regex]": "false",
        "columns[3][data]": "", "columns[3][name]": "", "columns[3][searchable]": "true", "columns[3][orderable]": "true", "columns[3][search][value]": "", "columns[3][search][regex]": "false",
        "columns[4][data]": "4", "columns[4][name]": "", "columns[4][searchable]": "false", "columns[4][orderable]": "true", "columns[4][search][value]": "", "columns[4][search][regex]": "false",
        "columns[5][data]": "5", "columns[5][name]": "", "columns[5][searchable]": "false", "columns[5][orderable]": "true", "columns[5][search][value]": "", "columns[5][search][regex]": "false",
        "columns[6][data]": "", "columns[6][name]": "", "columns[6][searchable]": "true", "columns[6][orderable]": "true", "columns[6][search][value]": "", "columns[6][search][regex]": "false",
        "columns[7][data]": "", "columns[7][name]": "", "columns[7][searchable]": "true", "columns[7][orderable]": "true", "columns[7][search][value]": "", "columns[7][search][regex]": "false",
        "columns[8][data]": "", "columns[8][name]": "", "columns[8][searchable]": "true", "columns[8][orderable]": "true", "columns[8][search][value]": "", "columns[8][search][regex]": "false",
        "columns[9][data]": "9", "columns[9][name]": "", "columns[9][searchable]": "false", "columns[9][orderable]": "true", "columns[9][search][value]": "", "columns[9][search][regex]": "false",
        "columns[10][data]": "", "columns[10][name]": "", "columns[10][searchable]": "true", "columns[10][orderable]": "false", "columns[10][search][value]": "", "columns[10][search][regex]": "false",
        "order[0][column]": "2",
        "order[0][dir]": "asc",
        "start": "0",
        "length": "-1",
        "search[value]": "",
        "search[regex]": "false",
        "_": "1764588130735"
    }
    r = await client.obtener_activosNoImplicados(params)
    r.raise_for_status()
    return {"step": "activos_no_implicados", "body": r.json()}

async def step_obtener_controlesImplicados(client: RiskClient, incidente_id: int) -> Dict[str, Any]:
    params = {
        "incidente": str(incidente_id),
        "draw": "2",
        "columns[0][data]": "0", "columns[0][name]": "", "columns[0][searchable]": "false", "columns[0][orderable]": "true", "columns[0][search][value]": "", "columns[0][search][regex]": "false",
        "columns[1][data]": "", "columns[1][name]": "", "columns[1][searchable]": "true", "columns[1][orderable]": "true", "columns[1][search][value]": "", "columns[1][search][regex]": "false",
        "columns[2][data]": "", "columns[2][name]": "", "columns[2][searchable]": "true", "columns[2][orderable]": "true", "columns[2][search][value]": "", "columns[2][search][regex]": "false",
        "columns[3][data]": "", "columns[3][name]": "", "columns[3][searchable]": "true", "columns[3][orderable]": "true", "columns[3][search][value]": "", "columns[3][search][regex]": "false",
        "columns[4][data]": "4", "columns[4][name]": "", "columns[4][searchable]": "false", "columns[4][orderable]": "true", "columns[4][search][value]": "", "columns[4][search][regex]": "false",
        "columns[5][data]": "5", "columns[5][name]": "", "columns[5][searchable]": "false", "columns[5][orderable]": "true", "columns[5][search][value]": "", "columns[5][search][regex]": "false",
        "columns[6][data]": "", "columns[6][name]": "", "columns[6][searchable]": "true", "columns[6][orderable]": "true", "columns[6][search][value]": "", "columns[6][search][regex]": "false",
        "columns[7][data]": "", "columns[7][name]": "", "columns[7][searchable]": "true", "columns[7][orderable]": "true", "columns[7][search][value]": "", "columns[7][search][regex]": "false",
        "columns[8][data]": "", "columns[8][name]": "", "columns[8][searchable]": "true", "columns[8][orderable]": "true", "columns[8][search][value]": "", "columns[8][search][regex]": "false",
        "columns[9][data]": "9", "columns[9][name]": "", "columns[9][searchable]": "false", "columns[9][orderable]": "true", "columns[9][search][value]": "", "columns[9][search][regex]": "false",
        "columns[10][data]": "", "columns[10][name]": "", "columns[10][searchable]": "true", "columns[10][orderable]": "false", "columns[10][search][value]": "", "columns[10][search][regex]": "false",
        "order[0][column]": "2",
        "order[0][dir]": "asc",
        "start": "0",
        "length": "-1",
        "search[value]": "",
        "search[regex]": "false",
        "_": "1764588130735"
    }
    r = await client.obtener_controlesImplicados(params)
    #r.raise_for_status()
    return {"step": "controles_implicados", "body": r.json()}

async def step_obtener_activosImplicados(client: RiskClient, incidente_id: int) -> Dict[str, Any]:
    params = {
        "incidente": str(incidente_id),
        "draw": "2",
        "columns[0][data]": "0", "columns[0][name]": "", "columns[0][searchable]": "false", "columns[0][orderable]": "true", "columns[0][search][value]": "", "columns[0][search][regex]": "false",
        "columns[1][data]": "", "columns[1][name]": "", "columns[1][searchable]": "true", "columns[1][orderable]": "true", "columns[1][search][value]": "", "columns[1][search][regex]": "false",
        "columns[2][data]": "", "columns[2][name]": "", "columns[2][searchable]": "true", "columns[2][orderable]": "true", "columns[2][search][value]": "", "columns[2][search][regex]": "false",
        "columns[3][data]": "", "columns[3][name]": "", "columns[3][searchable]": "true", "columns[3][orderable]": "false", "columns[3][search][value]": "", "columns[3][search][regex]": "false",
        "columns[4][data]": "", "columns[4][name]": "", "columns[4][searchable]": "true", "columns[4][orderable]": "false", "columns[4][search][value]": "", "columns[4][search][regex]": "false",
        "columns[5][data]": "", "columns[5][name]": "", "columns[5][searchable]": "true", "columns[5][orderable]": "false", "columns[5][search][value]": "", "columns[5][search][regex]": "false",
        "order[0][column]": "2",
        "order[0][dir]": "asc",
        "start": "0",
        "length": "-1",
        "search[value]": "",
        "search[regex]": "false",
        "_": "1764588130737"
    }
    r = await client.obtener_activosImplicados(params)
    r.raise_for_status()
    return {"step": "activos_implicados", "body": r.json()}

async def step_cargar_dimensionesClear(client: RiskClient, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
    if params is None:
        params = {"activo": "11", "incidente": "18"}
    r = await client.cargar_dimensionesClear(params)
    r.raise_for_status()
    return {"step": "cargar_dimensionesClear", "body": r.json()}

async def step_vincular_activo(client: RiskClient, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
    if params is None:
        params = {"dimension": "143", "activo": "", "incidente": "18", "porcentaje": "97", "vincular": "true", "activoAux": "11"}
    r = await client.vincular_activo(params)
    r.raise_for_status()
    return {"step": "vincular_activo", "body": r.json()}

async def step_vincular_control(client: RiskClient, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
    if params is None:
        params = {"control": "1716", "incidente": "18"}
    r = await client.vincular_control(params)
    r.raise_for_status()
    return {"step": "vincular_control", "body": r.json()}

async def step_recalcular(client: RiskClient) -> Dict[str, Any]:
    params = {
        "acam": "false",
        "ar": "true",
        "pdt": "false",
        "vr": "6",
        "con": "true",
        "po": "true",
        "dim": "true"
    }
    r = await client.recalcular(params)
    r.raise_for_status()
    return {"step": "recalcular", "body": r.json()}

async def step_ir_a_conclusion(client: RiskClient, id_evento: int) -> Dict[str, Any]:
    r = await client.ir_a_conclusion(id_evento)
    r.raise_for_status()
    return {"step": "ir_a_conclusion", "status_code": r.status_code}#, "body": r.json()}

async def step_guardar_y_cerrar(client: RiskClient, id_evento: int) -> Dict[str, Any]:
    settings = load_config()
    data = settings.new_conclusion
    
    if not data:
        raise ValueError("No se han encontrado datos de conclusion")
        
    '''content = "&".join([f"{k}={urllib.parse.quote_plus(str(v))}" for k, v in data.items()])
    print(content)'''

    files = {
            "save": (None, "Guardar"),
            "id": (None, "15"),
            "version": (None, "3"),
            "subproyecto": (None, "1"),
            "tipo": (None, "conclusion"),
            "cerrar": (None, "true"),
            "coste": (None, "11.00€"),
            "myCurrency": (None, "EUR"),
            "solucion": (None, "Solución"),
            "conclusion": (None, "Conclusión"),
            "evidencias[]": ("", b"", "application/octet-stream"),
        }
    
    r = await client.guardar_y_cerrar_evento(id_evento, files=files)
    #r.raise_for_status()
    return {"step": "guardar_y_cerrar",
    "status": r.status_code,
    "redirect": r.headers.get("Location")}

# --- Flow completo ---
async def run_all_flow(client: RiskClient, data: Dict[str, Any], emarisma_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    logger.info("Iniciando run_all_flow")
    results = []
    logger.info("Ejecutando step_login_exist")
    results.append(await step_login_exist(client))
    logger.info("Ejecutando step_authenticate")
    results.append(await step_authenticate(client))
    logger.info("Ejecutando step_get_projects")
    results.append(await step_get_projects(client))
    logger.info("Ejecutando step_get_subprojects")
    results.append(await step_get_subprojects(client, emarisma_data['subproyecto_id']))
    
    logger.info("obteniendo incidente_id y evento_id desde la base de datos")
    ids = await get_incidente_id_by_subproyecto_and_tipo_amenaza(emarisma_data['subproyecto_id'], emarisma_data['tipo_amenaza_instanciada_id'], data['user_id'])
    emarisma_data['incidente_id'] = ids['incidente_id']
    emarisma_data['evento_id'] = ids['evento_id']
    logger.info("Ejecutando step_guardar_gravedad")
    results.append(await step_guardar_gravedad(client, data, emarisma_data))
    logger.info("Ejecutando step_guardar_amenaza")
    results.append(await step_guardar_amenaza(client, emarisma_data)) 
    logger.info("Ejecutando step_obtener_eventos")
    results.append(await step_obtener_eventos(client, emarisma_data['subproyecto_id']))  # HASTA AQUI FUNCIONA 
    logger.info("Ejecutando step_cargar_incidente")
    results.append(await step_cargar_incidente(client, emarisma_data['incidente_id']))
    logger.info("Ejecutando step_obtener_controlesNoImplicados")
    results.append(await step_obtener_controlesNoImplicados(client, emarisma_data['incidente_id']))
    logger.info("Ejecutando step_obtener_activosNoImplicados")
    results.append(await step_obtener_activosNoImplicados(client, emarisma_data['incidente_id']))
    logger.info("Ejecutando step_obtener_controlesImplicados")
    results.append(await step_obtener_controlesImplicados(client, emarisma_data['incidente_id']))
    logger.info("Ejecutando step_obtener_activosImplicados")
    results.append(await step_obtener_activosImplicados(client, emarisma_data['incidente_id']))
    logger.info("Ejecutando step_cargar_dimensionesClear")
    results.append(await step_cargar_dimensionesClear(client, {"activo": str(emarisma_data['device_id']), "incidente": str(emarisma_data['incidente_id'])}))
    logger.info("Ejecutando step_vincular_activo")
    results.append(await step_vincular_activo(client, {"dimension": "143", "activo": "", "incidente": str(emarisma_data['incidente_id']), "porcentaje": "97", "vincular": "true", "activoAux": str(emarisma_data['device_id'])}))
    logger.info("Ejecutando step_vincular_control")
    results.append(await step_vincular_control(client, {"control": "1716", "incidente": str(emarisma_data['incidente_id'])}))
    logger.info("Ejecutando step_ir_a_conclusion")
    results.append(await step_ir_a_conclusion(client, emarisma_data['evento_id']))
    logger.info("Ejecutando step_guardar_y_cerrar")
    results.append(await step_guardar_y_cerrar(client, emarisma_data['evento_id']))
    logger.info("Ejecutando step_recalcular")
    results.append(await step_recalcular(client))
    logger.info("run_all_flow completado")
    return results
