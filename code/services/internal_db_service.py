import aiosqlite
from typing import List, Dict, Any
import os
import uuid
import json

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'internal.db')


async def init_db():
    """Inicializa la base de datos SQLite y crea tabla principal si no existe."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("PRAGMA encoding = 'UTF-8'")
        await db.execute("PRAGMA user_version = 1")
        await db.execute('''
            CREATE TABLE IF NOT EXISTS middleware_requests (
                id TEXT PRIMARY KEY,
                json_received TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'pending',
                riesgo_inherente_previo FLOAT,
                riesgo_inherente_nuevo FLOAT,
                riesgo_previo REAL,
                riesgo_nuevo REAL,
                valor_riesgo_previo FLOAT,
                valor_riesgo_nuevo FLOAT
            )
        ''')
        await db.commit()


async def save_request(json_received: Dict[str, Any]) -> str:
    """Guarda una petición en la base de datos interna con estado inicial pending."""
    request_id = str(uuid.uuid4())
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            '''
            INSERT INTO middleware_requests (id, json_received, status)
            VALUES (?, ?, 'pending')
            ''',
            (request_id, json.dumps(json_received, ensure_ascii=False))
        )
        await db.commit()
    return request_id


async def update_request_status(request_id: str, status: str):
    """Actualiza el estado de una petición en la máquina de estados interna."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            'UPDATE middleware_requests SET status = ? WHERE id = ?',
            (status, request_id)
        )
        await db.commit()


async def update_request_risk_previo(
    request_id: str,
    riesgo_inherente_previo: float = None,
    riesgo_previo: float = None,
    valor_riesgo_previo: float = None
):
    """Guarda los valores previos de riesgo en middleware_requests."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            '''
            UPDATE middleware_requests
            SET riesgo_inherente_previo = ?,
                riesgo_previo = ?,
                valor_riesgo_previo = ?
            WHERE id = ?
            ''',
            (riesgo_inherente_previo, riesgo_previo, valor_riesgo_previo, request_id)
        )
        await db.commit()


async def update_request_risk_nuevo(
    request_id: str,
    riesgo_inherente_nuevo: float = None,
    riesgo_nuevo: float = None,
    valor_riesgo_nuevo: float = None,
    status: str = 'completed'
):
    """Guarda los valores nuevos de riesgo y marca la petición como completed."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            '''
            UPDATE middleware_requests
            SET riesgo_inherente_nuevo = ?,
                riesgo_nuevo = ?,
                valor_riesgo_nuevo = ?,
                status = ?
            WHERE id = ?
            ''',
            (riesgo_inherente_nuevo, riesgo_nuevo, valor_riesgo_nuevo, status, request_id)
        )
        await db.commit()


async def get_request(request_id: str) -> Dict[str, Any]:
    """Obtiene una petición por ID con estado y valores de riesgo."""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            '''
            SELECT id, json_received, created_at, status,
                   riesgo_inherente_previo, riesgo_inherente_nuevo,
                   riesgo_previo, riesgo_nuevo,
                   valor_riesgo_previo, valor_riesgo_nuevo
            FROM middleware_requests
            WHERE id = ?
            ''',
            (request_id,)
        )
        row = await cursor.fetchone()
        if row:
            return {
                'id': row[0],
                'json_received': json.loads(row[1]),
                'created_at': row[2],
                'status': row[3],
                'riesgo_inherente_previo': row[4],
                'riesgo_inherente_nuevo': row[5],
                'riesgo_previo': row[6],
                'riesgo_nuevo': row[7],
                'valor_riesgo_previo': row[8],
                'valor_riesgo_nuevo': row[9],
            }
        return None


async def get_all_requests() -> List[Dict[str, Any]]:
    """Obtiene todas las peticiones con estado y valores de riesgo."""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            '''
            SELECT id, json_received, created_at, status,
                   riesgo_inherente_previo, riesgo_inherente_nuevo,
                   riesgo_previo, riesgo_nuevo,
                   valor_riesgo_previo, valor_riesgo_nuevo
            FROM middleware_requests
            '''
        )
        rows = await cursor.fetchall()
        return [
            {
                'id': row[0],
                'json_received': json.loads(row[1]),
                'created_at': row[2],
                'status': row[3],
                'riesgo_inherente_previo': row[4],
                'riesgo_inherente_nuevo': row[5],
                'riesgo_previo': row[6],
                'riesgo_nuevo': row[7],
                'valor_riesgo_previo': row[8],
                'valor_riesgo_nuevo': row[9],
            }
            for row in rows
        ]
