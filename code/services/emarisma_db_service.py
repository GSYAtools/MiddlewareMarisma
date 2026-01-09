import aiomysql
import json
import asyncio
from fastapi import HTTPException
import logging
from typing import Dict

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

async def get_tipo_amenaza_instanciada_id_by_subproyecto_and_nombre(subproyecto_id: int, nombre: str) -> int:
    """
    Obtiene el tipo_amenaza_instanciada_id de la tabla amenaza_instanciada por subproyecto_id y nombre.
    """
    logger.info(f"Buscando tipo_amenaza_instanciada_id para subproyecto_id: {subproyecto_id}, nombre: {nombre}")
    try:
        db_pool = await get_db_pool()
        async with db_pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute(
                    "SELECT tipo_amenaza_instanciada_id FROM amenaza_instanciada WHERE subproyecto_id = %s AND nombre = %s AND deleted = 0",
                    (subproyecto_id, nombre)
                )
                result = await cursor.fetchone()
                tipo_amenaza_id = result['tipo_amenaza_instanciada_id'] if result else None
                logger.info(f"tipo_amenaza_instanciada_id encontrado: {tipo_amenaza_id}")
                return tipo_amenaza_id
    except Exception as e:
        logger.warning(f"Error al buscar tipo_amenaza_instanciada_id para subproyecto '{subproyecto_id}', nombre '{nombre}': {e}. Usando ID dummy 690 para testing.")
        return 690

async def get_incidente_id_by_subproyecto_and_tipo_amenaza(subproyecto_id: int, tipo_amenaza_instanciada_id: int, user_id: str) -> Dict[str, int]:
    """
    Obtiene el incidente_id y evento_id más recientes para el subproyecto y tipo de amenaza.
    Primero obtiene el último evento para el subproyecto y usuario, luego encuentra el incidente correspondiente.
    """
    logger.info(f"Buscando incidente_id para subproyecto_id: {subproyecto_id}, tipo_amenaza_instanciada_id: {tipo_amenaza_instanciada_id}, user_id: {user_id}")
    try:
        db_pool = await get_db_pool()
        async with db_pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                # Obtener el último evento para el subproyecto y usuario
                await cursor.execute(
                    "SELECT id FROM evento WHERE subproyecto_id = %s AND responsable = %s AND deleted = 0 ORDER BY id DESC LIMIT 1",
                    (subproyecto_id, user_id)
                )
                evento_result = await cursor.fetchone()
                if not evento_result:
                    raise ValueError(f"No se encontró evento para subproyecto {subproyecto_id} y usuario {user_id}")
                evento_id = evento_result['id']
                logger.info(f"Evento ID encontrado: {evento_id}")

                # Obtener amenaza_instanciada_id
                await cursor.execute(
                    "SELECT id FROM amenaza_instanciada WHERE tipo_amenaza_instanciada_id = %s AND subproyecto_id = %s AND deleted = 0",
                    (tipo_amenaza_instanciada_id, subproyecto_id)
                )
                amenaza_result = await cursor.fetchone()
                if not amenaza_result:
                    raise ValueError(f"No se encontró amenaza_instanciada para tipo {tipo_amenaza_instanciada_id} y subproyecto {subproyecto_id}")
                amenaza_instanciada_id = amenaza_result['id']
                logger.info(f"Amenaza instanciada ID encontrada: {amenaza_instanciada_id}")

                # Obtener incidente_id
                await cursor.execute(
                    "SELECT id FROM incidente WHERE evento_id = %s AND amenaza_instanciada_id = %s AND deleted = 0",
                    (evento_id, amenaza_instanciada_id)
                )
                incidente_result = await cursor.fetchone()
                if not incidente_result:
                    raise ValueError(f"No se encontró incidente para evento {evento_id} y amenaza {amenaza_instanciada_id}")
                incidente_id = incidente_result['id']
                logger.info(f"Incidente ID encontrado: {incidente_id}")
                return {"incidente_id": incidente_id, "evento_id": evento_id}
    except Exception as e:
        logger.error(f"Error al buscar incidente_id: {e}")
        raise