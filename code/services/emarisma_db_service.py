import aiomysql
import json
import asyncio
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)

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
        "db": config["db_name"]
    }

async def get_db_pool():
    """
    Inicializa y devuelve el pool de conexiones a la base de datos.
    Si el pool ya existe, lo devuelve directamente.
    """
    global pool
    if pool is None:
        config = load_db_config()
        loop = asyncio.get_running_loop()
        pool = await aiomysql.create_pool(
            **config,
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
    logger.info(f"Buscando ID del proyecto con nombre: {name}")
    try:
        db_pool = await get_db_pool()
        async with db_pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute("SELECT id FROM proyecto WHERE nombre = %s", (name,))
                result = await cursor.fetchone()
                proyecto_id = result['id'] if result else None
                logger.info(f"ID del proyecto encontrado: {proyecto_id}")
                return proyecto_id
    except Exception as e:
        logger.warning(f"Error al buscar proyecto '{name}': {e}. Usando ID dummy 1 para testing.")
        return 1

async def get_subproyecto_id_by_name(name: str) -> int:
    """
    Obtiene el ID del subproyecto por nombre.
    """
    logger.info(f"Buscando ID del subproyecto con nombre: {name}")
    try:
        db_pool = await get_db_pool()
        async with db_pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute("SELECT id FROM subproyecto WHERE nombre = %s", (name,))
                result = await cursor.fetchone()
                subproyecto_id = result['id'] if result else None
                logger.info(f"ID del subproyecto encontrado: {subproyecto_id}")
                return subproyecto_id
    except Exception as e:
        logger.warning(f"Error al buscar subproyecto '{name}': {e}. Usando ID dummy 1 para testing.")
        return 1