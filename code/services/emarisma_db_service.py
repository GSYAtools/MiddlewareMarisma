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
    Retorna None si no se encuentra.
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
        logger.error(f"Error al buscar proyecto '{name}': {e}")
        return None

async def get_subproyecto_id_by_name(name: str) -> int:
    """
    Obtiene el ID del subproyecto por nombre.
    Retorna None si no se encuentra.
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
        logger.error(f"Error al buscar subproyecto '{name}': {e}")
        return None

async def get_tipo_amenaza_instanciada_id_by_subproyecto_and_nombre(subproyecto_id: int, nombre: str) -> int:
    """
    Obtiene el tipo_amenaza_instanciada_id de la tabla amenaza_instanciada por subproyecto_id y nombre.
    Retorna None si no se encuentra.
    """
    logger.info(f"Buscando amenaza_instanciada_id para subproyecto_id: {subproyecto_id}, nombre: {nombre}")
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
                logger.info(f"amenaza_instanciada_id encontrado: {tipo_amenaza_id}")
                return tipo_amenaza_id
    except Exception as e:
        logger.error(f"Error al buscar amenaza_instanciada_id para subproyecto '{subproyecto_id}', nombre '{nombre}': {e}")
        return None

async def get_activo_id_by_name(name: str) -> int:
    """
    Obtiene el ID del activo por nombre.
    Retorna None si no se encuentra.
    """
    logger.info(f"Buscando ID del activo con nombre: {name}")
    try:
        db_pool = await get_db_pool()
        async with db_pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute("SELECT id FROM activo WHERE nombre = %s AND deleted = 0", (name,))
                result = await cursor.fetchone()
                activo_id = result['id'] if result else None
                logger.info(f"ID del activo encontrado: {activo_id}")
                return activo_id
    except Exception as e:
        logger.error(f"Error al buscar activo '{name}': {e}")
        return None

async def get_amenaza_instanciada_id(tipo_amenaza_instanciada_id: int, subproyecto_id: int) -> int:
    """
    Obtiene el amenaza_instanciada_id desde tipo_amenaza_instanciada_id y subproyecto_id.
    Retorna None si no se encuentra.
    """
    logger.info(f"Buscando amenaza_instanciada_id para tipo_amenaza_instanciada_id: {tipo_amenaza_instanciada_id}, subproyecto_id: {subproyecto_id}")
    try:
        db_pool = await get_db_pool()
        async with db_pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute(
                    "SELECT id FROM amenaza_instanciada WHERE tipo_amenaza_instanciada_id = %s AND subproyecto_id = %s AND deleted = 0",
                    (tipo_amenaza_instanciada_id, subproyecto_id)
                )
                result = await cursor.fetchone()
                amenaza_instanciada_id = result['id'] if result else None
                logger.info(f"amenaza_instanciada_id encontrado: {amenaza_instanciada_id}")
                return amenaza_instanciada_id
    except Exception as e:
        logger.error(f"Error al buscar amenaza_instanciada_id para tipo {tipo_amenaza_instanciada_id} y subproyecto {subproyecto_id}: {e}")
        return None

async def get_activo_amenaza_id(amenaza_instanciada_id: int, activo_id: int) -> int:
    """
    Obtiene el activo_amenaza_id desde amenaza_instanciada_id y activo_id.
    Retorna None si no se encuentra.
    """
    logger.info(f"Buscando activo_amenaza_id para amenaza_instanciada_id: {amenaza_instanciada_id}, activo_id: {activo_id}")
    try:
        db_pool = await get_db_pool()
        async with db_pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute(
                    "SELECT id FROM activo_amenaza WHERE amenaza_instanciada_id = %s AND activo_id = %s AND deleted = 0",
                    (amenaza_instanciada_id, activo_id)
                )
                result = await cursor.fetchone()
                activo_amenaza_id = result['id'] if result else None
                logger.info(f"activo_amenaza_id encontrado: {activo_amenaza_id}")
                return activo_amenaza_id
    except Exception as e:
        logger.error(f"Error al buscar activo_amenaza_id para amenaza {amenaza_instanciada_id} y activo {activo_id}: {e}")
        return None

async def get_dimension_ids_by_activo_amenaza(activo_amenaza_id: int) -> list[int]:
    """
    Obtiene todos los dimension_instanciada_id que corresponden a un activo_amenaza_id.
    Retorna lista vacía si no se encuentran.
    """
    logger.info(f"Buscando dimension_instanciada_ids para activo_amenaza_id: {activo_amenaza_id}")
    try:
        db_pool = await get_db_pool()
        async with db_pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute(
                    "SELECT dimension_instanciada_id FROM activo_amenaza_dimension WHERE activo_amenaza_id = %s AND deleted = 0",
                    (activo_amenaza_id,)
                )
                results = await cursor.fetchall()
                dimension_ids = [row['dimension_instanciada_id'] for row in results if row['dimension_instanciada_id'] is not None]
                logger.info(f"dimension_instanciada_ids encontrados: {dimension_ids}")
                return dimension_ids
    except Exception as e:
        logger.error(f"Error al buscar dimension_instanciada_ids para activo_amenaza {activo_amenaza_id}: {e}")
        return []

async def verificar_evento_existe(evento_id: int) -> bool:
    """
    Verifica si un evento existe en la base de datos.
    """
    logger.info(f"Verificando si existe evento_id: {evento_id}")
    try:
        db_pool = await get_db_pool()
        async with db_pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute(
                    "SELECT id, subproyecto_id, responsable, descripcion FROM evento WHERE id = %s AND deleted = 0",
                    (evento_id,)
                )
                resultado = await cursor.fetchone()
                existe = resultado is not None
                if existe:
                    logger.info(f"✓ Evento {evento_id} confirmado: subproyecto={resultado['subproyecto_id']}, responsable={resultado['responsable']}")
                else:
                    logger.error(f"✗ Evento {evento_id} NO existe en la BD")
                return existe
    except Exception as e:
        logger.error(f"Error al verificar evento {evento_id}: {e}")
        return False

async def verificar_incidente_existe(evento_id: int, amenaza_instanciada_id: int) -> dict:
    """
    Verifica si existe un incidente para evento_id Y amenaza_instanciada_id y retorna sus detalles.
    """
    logger.info(f"Verificando si existe incidente para evento_id: {evento_id}, amenaza_instanciada_id: {amenaza_instanciada_id}")
    try:
        db_pool = await get_db_pool()
        async with db_pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute(
                    "SELECT id, evento_id, amenaza_instanciada_id, gravedad FROM incidente WHERE evento_id = %s AND amenaza_instanciada_id = %s AND deleted = 0",
                    (evento_id, amenaza_instanciada_id)
                )
                resultado = await cursor.fetchone()
                if resultado:
                    logger.info(f"✓ Incidente confirmado: id={resultado['id']}, amenaza_instanciada_id={resultado['amenaza_instanciada_id']}, gravedad={resultado['gravedad']}")
                    return dict(resultado)
                else:
                    logger.warning(f"✗ NO existe incidente para evento {evento_id} y amenaza {amenaza_instanciada_id}")
                    return None
    except Exception as e:
        logger.error(f"Error al verificar incidente para evento {evento_id} y amenaza {amenaza_instanciada_id}: {e}")
        return None

async def get_incidente_id_by_evento(evento_id: int, amenaza_instanciada_id: int) -> Dict[str, int]:
    """
    Obtiene el incidente_id para evento_id Y amenaza_instanciada_id específicos.
    """
    logger.info(f"Buscando incidente_id para evento_id: {evento_id}, amenaza_instanciada_id: {amenaza_instanciada_id}")
    try:
        db_pool = await get_db_pool()
        async with db_pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute(
                    "SELECT id, amenaza_instanciada_id FROM incidente WHERE evento_id = %s AND amenaza_instanciada_id = %s AND deleted = 0 ORDER BY id DESC LIMIT 1",
                    (evento_id, amenaza_instanciada_id)
                )
                resultado = await cursor.fetchone()
                if not resultado:
                    logger.warning(f"No se encontró ningún incidente para evento {evento_id} y amenaza {amenaza_instanciada_id}")
                    return None
                logger.info(f"Incidente encontrado: id={resultado['id']}, amenaza_instanciada_id={resultado['amenaza_instanciada_id']}")
                return {"incidente_id": resultado['id'], "amenaza_instanciada_id": resultado['amenaza_instanciada_id']}
    except Exception as e:
        logger.error(f"Error al buscar incidente para evento {evento_id} y amenaza {amenaza_instanciada_id}: {e}")
        return None

async def get_evento_id_by_subproyecto_and_user(subproyecto_id: int, user_id: str) -> int:
    """
    Obtiene el evento_id más reciente para el subproyecto y usuario.
    Retorna None si no se encuentra.
    """
    logger.info(f"Buscando evento_id para subproyecto_id: {subproyecto_id}, user_id: {user_id}")
    try:
        db_pool = await get_db_pool()
        async with db_pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute(
                    "SELECT id FROM evento WHERE subproyecto_id = %s AND responsable = %s AND deleted = 0 ORDER BY id DESC LIMIT 1",
                    (subproyecto_id, user_id)
                )
                resultado = await cursor.fetchone()
                evento_id = resultado['id'] if resultado else None
                logger.info(f"Evento ID encontrado: {evento_id}")
                return evento_id
    except Exception as e:
        logger.error(f"Error al buscar evento_id: {e}")
        return None

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
                evento_id = await get_evento_id_by_subproyecto_and_user(subproyecto_id, user_id)
                if not evento_id:
                    raise ValueError(f"No se encontró evento para subproyecto {subproyecto_id} y usuario {user_id}")
                logger.info(f"Evento ID encontrado: {evento_id}")

                # Obtener amenaza_instanciada_id
                amenaza_instanciada_id = await get_amenaza_instanciada_id(tipo_amenaza_instanciada_id, subproyecto_id)
                if not amenaza_instanciada_id:
                    raise ValueError(f"No se encontró amenaza_instanciada para tipo {tipo_amenaza_instanciada_id} y subproyecto {subproyecto_id}")
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