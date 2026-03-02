import aiomysql
import json
import asyncio
from fastapi import HTTPException
import logging
from typing import Dict
import os

logger = logging.getLogger(__name__)

# Variable global para el pool de conexiones
pool = None
db_config_cache = None


def _is_db_connection_error(exc: Exception) -> bool:
    if isinstance(exc, (OSError, TimeoutError, ConnectionError)):
        return True
    error_code = exc.args[0] if getattr(exc, "args", None) else None
    return error_code in {2002, 2003, 2006, 2013, 2055}


def _raise_db_unavailable(exc: Exception):
    logger.error(f"Base de datos eMarisma no disponible: {exc}")
    raise HTTPException(
        status_code=503,
        detail="No hay conexión con la base de datos eMarisma. Intenta de nuevo más tarde."
    )

def load_db_config():
    """Carga la configuración de la base de datos desde config.json."""
    with open("config.json", "r") as file:
        config = json.load(file)
    return {
        "host": os.getenv("DB_HOST", config["db_host"]),
        "port": int(os.getenv("DB_PORT", config["db_port"])),
        "user": os.getenv("DB_USER", config["db_user"]),
        "password": os.getenv("DB_PASSWORD", config["db_password"]),
        "db": os.getenv("DB_NAME", config["db_name"]),
        "connect_timeout": int(os.getenv("DB_CONNECT_TIMEOUT", config.get("db_connect_timeout", 10))),
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
        try:
            pool = await aiomysql.create_pool(
                **config,
                loop=loop,
                autocommit=True,
                pool_recycle=300,
            )
        except Exception as e:
            if _is_db_connection_error(e):
                fallback_host = os.getenv("DB_HOST_FALLBACK", "host.docker.internal")
                if config.get("host") != fallback_host:
                    logger.warning(
                        "No se pudo conectar a MySQL en %s. Reintentando con host fallback %s",
                        config.get("host"),
                        fallback_host,
                    )
                    fallback_config = dict(config)
                    fallback_config["host"] = fallback_host
                    try:
                        pool = await aiomysql.create_pool(
                            **fallback_config,
                            loop=loop,
                            autocommit=True,
                            pool_recycle=300,
                        )
                        logger.info("Conexión MySQL establecida usando host fallback %s", fallback_host)
                        return pool
                    except Exception as fallback_error:
                        if _is_db_connection_error(fallback_error):
                            _raise_db_unavailable(fallback_error)
                        raise
                _raise_db_unavailable(e)
            raise
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
        if _is_db_connection_error(e):
            global pool
            pool = None
            _raise_db_unavailable(e)
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
        if _is_db_connection_error(e):
            global pool
            pool = None
            _raise_db_unavailable(e)
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
        if _is_db_connection_error(e):
            global pool
            pool = None
            _raise_db_unavailable(e)
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
        if _is_db_connection_error(e):
            global pool
            pool = None
            _raise_db_unavailable(e)
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

async def get_risk_values_by_activo_amenaza(activo_amenaza_id: int) -> Dict[str, float]:
    """
    Obtiene los valores de riesgo más recientes desde analisis_riesgo para un activo_amenaza.
    Retorna None si no encuentra resultados.
    """
    logger.info(f"Buscando riesgos en analisis_riesgo para activo_amenaza_id: {activo_amenaza_id}")
    try:
        db_pool = await get_db_pool()
        async with db_pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute(
                    '''
                    SELECT riesgo_inherente, riesgo, valor_riesgo
                    FROM analisis_riesgo
                    WHERE activo_amenaza_id = %s AND deleted = 0
                    ORDER BY id DESC
                    LIMIT 1
                    ''',
                    (activo_amenaza_id,)
                )
                result = await cursor.fetchone()
                if not result:
                    logger.warning(
                        f"No se encontraron riesgos para activo_amenaza_id: {activo_amenaza_id}"
                    )
                    return None

                risk_values = {
                    "riesgo_inherente": float(result["riesgo_inherente"]),
                    "riesgo": float(result["riesgo"]),
                    "valor_riesgo": float(result["valor_riesgo"]),
                }
                logger.info(
                    "Riesgos encontrados para activo_amenaza_id %s: %s",
                    activo_amenaza_id,
                    risk_values,
                )
                return risk_values
    except Exception as e:
        logger.error(f"Error al buscar riesgos para activo_amenaza_id {activo_amenaza_id}: {e}")
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

async def get_first_control_for_amenaza(amenaza_instanciada_id: int) -> int:
    """
    Obtiene el primer control disponible para una amenaza instanciada.
    Retorna None si no se encuentra ningún control.
    """
    logger.info(f"Buscando primer control para amenaza_instanciada_id: {amenaza_instanciada_id}")
    try:
        db_pool = await get_db_pool()
        async with db_pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute(
                    "SELECT control_instanciado_id FROM control_amenaza_instanciado WHERE amenaza_instanciada_id = %s LIMIT 1",
                    (amenaza_instanciada_id,)
                )
                result = await cursor.fetchone()
                control_id = result['control_instanciado_id'] if result else None
                logger.info(f"Primer control encontrado: {control_id}")
                return control_id
    except Exception as e:
        logger.error(f"Error al buscar primer control para amenaza {amenaza_instanciada_id}: {e}")
        return None

async def get_controls_by_codes_for_amenaza(amenaza_instanciada_id: int, control_codes: list[str]) -> list[int]:
    """
    Obtiene los control_instanciado_id que corresponden a una lista de códigos y una amenaza instanciada.
    Retorna lista de control_instanciado_id encontrados.
    Lanza HTTPException si algún código no corresponde a la amenaza.
    """
    logger.info(f"Buscando controles para amenaza_instanciada_id: {amenaza_instanciada_id}, códigos: {control_codes}")
    
    # Validación: la lista de códigos no puede estar vacía
    if not control_codes:
        logger.error("La lista de códigos de control está vacía")
        raise HTTPException(status_code=400, detail="La lista de códigos de control no puede estar vacía")
    
    # Validación: amenaza_instanciada_id debe ser positivo
    if not isinstance(amenaza_instanciada_id, int) or amenaza_instanciada_id <= 0:
        logger.error(f"ID de amenaza inválido: {amenaza_instanciada_id}")
        raise HTTPException(status_code=400, detail="ID de amenaza inválido")
    
    try:
        db_pool = await get_db_pool()
        async with db_pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                # Construir condiciones LIKE para todos los códigos usando OR
                # Nota: solo se interpola la cantidad de placeholders, no los valores del usuario
                like_conditions = ' OR '.join(['ci.codigo LIKE %s'] * len(control_codes))
                query = f"""
                    SELECT cai.control_instanciado_id, ci.codigo 
                    FROM control_amenaza_instanciado cai 
                    JOIN control_instanciado ci ON ci.id = cai.control_instanciado_id 
                    WHERE cai.amenaza_instanciada_id = %s 
                    AND ({like_conditions})
                """
                # Sanitizar y preparar los parámetros para LIKE
                # Los wildcards % y _ en SQL LIKE tienen significado especial, los escapamos
                # para buscar literalmente los códigos de control
                like_params = []
                for code in control_codes:
                    # Escapar caracteres especiales de LIKE: % y _
                    sanitized_code = code.replace('\\', '\\\\').replace('%', '\\%').replace('_', '\\_')
                    like_params.append(f"%{sanitized_code}%")
                
                # Ejecutar consulta con parámetros totalmente sanitizados
                await cursor.execute(query, (amenaza_instanciada_id, *like_params))
                results = await cursor.fetchall()
                
                # Mapear códigos encontrados con los solicitados
                found_controls = {}
                for row in results:
                    # Buscar a qué código solicitado corresponde este resultado
                    for requested_code in control_codes:
                        if requested_code in row['codigo']:
                            found_controls[requested_code] = row['control_instanciado_id']
                            break
                
                control_ids = list(found_controls.values())
                
                # Verificar si algún código no fue encontrado
                missing_codes = set(control_codes) - set(found_controls.keys())
                if missing_codes:
                    missing_str = ', '.join(missing_codes)
                    error_msg = f"Control Not Applicable for Threat {amenaza_instanciada_id}: {missing_str}"
                    logger.error(error_msg)
                    raise HTTPException(status_code=400, detail=error_msg)
                
                logger.info(f"Controles encontrados: {control_ids} para códigos: {list(found_controls.keys())}")
                return control_ids
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error al buscar controles para amenaza {amenaza_instanciada_id}: {e}")
        raise HTTPException(status_code=500, detail=f"Error al buscar controles: {str(e)}")