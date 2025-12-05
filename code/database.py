import aiomysql
import json
import asyncio
from fastapi import HTTPException

# Variable global para el pool de conexiones
pool = None
db_config_cache = None

def load_db_config():
    """Carga la configuración de la base de datos desde config.json."""
    with open("config.json", "r") as file:
        config = json.load(file)
    return {
        "host": config["db_host"],
        "port": config["db_port"],
        "user": config["db_user"],
        "password": config["db_password"],
        "db": config["db_name"],
        "subproyecto_id": config["subproyecto_id"]
    }

async def get_db_pool():
    """
    Inicializa y devuelve el pool de conexiones a la base de datos.
    Si el pool ya existe, lo devuelve directamente.
    """
    global pool
    if pool is None:
        config = load_db_config()
        # Excluimos subproyecto_id porque no es un parámetro de aiomysql
        db_connect_config = {k: v for k, v in config.items() if k != 'subproyecto_id'}
        loop = asyncio.get_running_loop()
        pool = await aiomysql.create_pool(
            **db_connect_config,
            loop=loop,
            autocommit=True # Autocommit para simplificar las operaciones
        )
    return pool

async def get_db_connection():
    """Función de dependencia de FastAPI para obtener una conexión del pool."""
    db_pool = await get_db_pool()
    async with db_pool.acquire() as conn:
        yield conn

async def get_risk_analysis(conn: aiomysql.Connection, activo_id: int, codigo_amenaza: str):
    """
    Ejecuta la lógica de consultas para obtener el análisis de riesgo.
    """
    global db_config_cache
    if db_config_cache is None:
        db_config_cache = load_db_config()

    subproyecto_id = int(db_config_cache['subproyecto_id'])

    activo_amenaza_id = None

    # 1. Primera consulta para obtener activo_amenaza_id
    query_get_id = """
        SELECT 
            am.id AS activo_amenaza_id
        FROM ar_marisma.activo_amenaza am
            INNER JOIN ar_marisma.amenaza_instanciada ami ON am.amenaza_instanciada_id = ami.id
        WHERE 
            ami.subproyecto_id = %s
            AND am.activo_id = %s
            AND ami.codigo = %s
            AND am.deleted = 0
            AND ami.deleted = 0;
    """
    async with conn.cursor(aiomysql.DictCursor) as cursor:
        await cursor.execute(query_get_id, (subproyecto_id, activo_id, int(codigo_amenaza)))
        result = await cursor.fetchone()
        if result:
            activo_amenaza_id = int(result['activo_amenaza_id'])

    if not activo_amenaza_id:
        return None # O lanzar una excepción si se prefiere

    # 2. Segunda consulta principal
    query_main = """
        SELECT 
            ami.subproyecto_id,
            ar.activo_amenaza_id,
            act.nombre AS nombre_activo,
            act.valor_estrategico,
            ami.codigo AS codigo_amenaza,
            ami.nombre AS nombre_amenaza,
            ar.riesgo_inherente,
            ar.impacto_total,
            ar.vulnerabilidad,
            ar.riesgo AS riesgo_residual,
            ar.valor_riesgo AS nivel_riesgo
        FROM ar_marisma.analisis_riesgo ar
            INNER JOIN ar_marisma.activo_amenaza am ON ar.activo_amenaza_id = am.id
            INNER JOIN ar_marisma.activo act ON am.activo_id = act.id
            INNER JOIN ar_marisma.amenaza_instanciada ami ON am.amenaza_instanciada_id = ami.id
        WHERE 
            ar.deleted = 0 
            AND am.deleted = 0
            AND ami.subproyecto_id = %s
            AND ar.activo_amenaza_id = %s;
    """
    async with conn.cursor(aiomysql.DictCursor) as cursor:
        await cursor.execute(query_main, (subproyecto_id, activo_amenaza_id))
        analysis_result = await cursor.fetchone()
        return analysis_result