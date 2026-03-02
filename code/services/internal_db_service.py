import aiosqlite
from typing import List, Dict, Any
import os
import uuid
from datetime import datetime
import json

# Ruta de la base de datos SQLite interna
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'internal.db')

STATUS_PENDING = "PENDING"
STATUS_COMPLETED = "COMPLETED"


def _safe_json_load(value: str | None) -> Dict[str, Any] | None:
    if not value:
        return None
    try:
        return json.loads(value)
    except Exception:
        return None


async def init_db():
    """Inicializa la base de datos SQLite y crea/migra tablas necesarias."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("PRAGMA encoding = 'UTF-8'")
        await db.execute("PRAGMA user_version = 2")

        await db.execute('''
            CREATE TABLE IF NOT EXISTS middleware_requests (
                id TEXT PRIMARY KEY,
                json_received TEXT NOT NULL,
                emarisma_data TEXT,
                risk_before TEXT,
                risk_after TEXT,
                status TEXT NOT NULL DEFAULT 'PENDING' CHECK (status IN ('PENDING', 'COMPLETED')),
                completed_at TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        cursor = await db.execute("PRAGMA table_info(middleware_requests)")
        columns = [row[1] for row in await cursor.fetchall()]

        if "emarisma_data" not in columns:
            await db.execute("ALTER TABLE middleware_requests ADD COLUMN emarisma_data TEXT")
        if "risk_before" not in columns:
            await db.execute("ALTER TABLE middleware_requests ADD COLUMN risk_before TEXT")
        if "risk_after" not in columns:
            await db.execute("ALTER TABLE middleware_requests ADD COLUMN risk_after TEXT")
        if "status" not in columns:
            await db.execute("ALTER TABLE middleware_requests ADD COLUMN status TEXT NOT NULL DEFAULT 'PENDING'")
            await db.execute("UPDATE middleware_requests SET status = 'PENDING' WHERE status IS NULL OR status = ''")
        if "completed_at" not in columns:
            await db.execute("ALTER TABLE middleware_requests ADD COLUMN completed_at TIMESTAMP")

        legacy_exists_cursor = await db.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='emarisma_data'"
        )
        legacy_exists = await legacy_exists_cursor.fetchone()
        if legacy_exists:
            await db.execute('''
                UPDATE middleware_requests
                SET emarisma_data = (
                    SELECT e.data
                    FROM emarisma_data e
                    WHERE e.request_id = middleware_requests.id
                )
                WHERE emarisma_data IS NULL
            ''')

        await db.commit()


async def save_request(json_received: Dict[str, Any], emarisma_data: Dict[str, Any] = None) -> str:
    """Guarda una petición en la base de datos interna con estado PENDING."""
    request_id = str(uuid.uuid4())
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            '''
            INSERT INTO middleware_requests (id, json_received, emarisma_data, status)
            VALUES (?, ?, ?, ?)
            ''',
            (
                request_id,
                json.dumps(json_received, ensure_ascii=False),
                json.dumps(emarisma_data, ensure_ascii=False) if emarisma_data else None,
                STATUS_PENDING,
            )
        )
        await db.commit()
    return request_id


async def update_emarisma_data(request_id: str, emarisma_data: Dict[str, Any]):
    """Actualiza los datos asociados de eMarisma para una petición."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            'UPDATE middleware_requests SET emarisma_data = ? WHERE id = ?',
            (json.dumps(emarisma_data, ensure_ascii=False), request_id)
        )
        await db.commit()


async def update_initial_risk_snapshot(request_id: str, risk_before: Dict[str, Any]):
    """Guarda snapshot inicial de riesgos y mantiene estado PENDING."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            '''
            UPDATE middleware_requests
            SET risk_before = ?, status = ?
            WHERE id = ?
            ''',
            (json.dumps(risk_before, ensure_ascii=False), STATUS_PENDING, request_id)
        )
        await db.commit()


async def mark_request_completed(
    request_id: str,
    risk_after: Dict[str, Any],
    emarisma_data: Dict[str, Any] | None = None
):
    """Marca la petición como COMPLETED y guarda snapshot final de riesgos."""
    completed_at = datetime.utcnow().isoformat()
    async with aiosqlite.connect(DB_PATH) as db:
        if emarisma_data is not None:
            await db.execute(
                '''
                UPDATE middleware_requests
                SET risk_after = ?, emarisma_data = ?, status = ?, completed_at = ?
                WHERE id = ?
                ''',
                (
                    json.dumps(risk_after, ensure_ascii=False),
                    json.dumps(emarisma_data, ensure_ascii=False),
                    STATUS_COMPLETED,
                    completed_at,
                    request_id,
                )
            )
        else:
            await db.execute(
                '''
                UPDATE middleware_requests
                SET risk_after = ?, status = ?, completed_at = ?
                WHERE id = ?
                ''',
                (
                    json.dumps(risk_after, ensure_ascii=False),
                    STATUS_COMPLETED,
                    completed_at,
                    request_id,
                )
            )
        await db.commit()


async def get_request(request_id: str) -> Dict[str, Any]:
    """Obtiene una petición por ID con su estado y snapshots de riesgo."""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            '''
            SELECT id, json_received, emarisma_data, risk_before, risk_after, status, created_at, completed_at
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
                'emarisma_data': _safe_json_load(row[2]),
                'risk_before': _safe_json_load(row[3]),
                'risk_after': _safe_json_load(row[4]),
                'status': row[5],
                'created_at': row[6],
                'completed_at': row[7],
            }
        return None


async def get_request_completed(request_id: str) -> Dict[str, Any]:
    """Obtiene una petición sólo si está COMPLETED."""
    request_data = await get_request(request_id)
    if not request_data:
        return None
    if request_data.get('status') != STATUS_COMPLETED:
        return None
    return request_data


async def get_all_requests() -> List[Dict[str, Any]]:
    """Obtiene todas las peticiones con su estado y snapshots de riesgo."""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            '''
            SELECT id, json_received, emarisma_data, risk_before, risk_after, status, created_at, completed_at
            FROM middleware_requests
            '''
        )
        rows = await cursor.fetchall()
        return [
            {
                'id': row[0],
                'json_received': json.loads(row[1]),
                'emarisma_data': _safe_json_load(row[2]),
                'risk_before': _safe_json_load(row[3]),
                'risk_after': _safe_json_load(row[4]),
                'status': row[5],
                'created_at': row[6],
                'completed_at': row[7],
            }
            for row in rows
        ]

# Inicializar la DB al importar (solo para desarrollo; en producción, llamar init_db() en startup)
# asyncio.run(init_db())  # Comentado para evitar ejecución automática
