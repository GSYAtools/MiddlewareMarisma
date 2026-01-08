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

async def get_proyecto_id_by_name(name: str) -> int:
    """
    Obtiene el ID del proyecto por nombre.
    """
    async with get_db_connection() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("SELECT id FROM proyectos WHERE nombre = %s", (name,))
            result = await cursor.fetchone()
            return result['id'] if result else None

async def get_subproyecto_id_by_name(name: str) -> int:
    """
    Obtiene el ID del subproyecto por nombre.
    """
    async with get_db_connection() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("SELECT id FROM subproyectos WHERE nombre = %s", (name,))
            result = await cursor.fetchone()
            return result['id'] if result else None