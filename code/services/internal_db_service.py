import sqlite3
import asyncio
import aiosqlite
from typing import List, Dict, Any
import os
import uuid
from datetime import datetime

# Ruta de la base de datos SQLite interna
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'internal.db')

async def init_db():
    """Inicializa la base de datos SQLite y crea tablas si no existen."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS middleware_requests (
                id TEXT PRIMARY KEY,
                json_received TEXT NOT NULL,
                emarisma_data TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        await db.commit()

async def save_request(json_received: Dict[str, Any], emarisma_data: Dict[str, Any] = None) -> str:
    """Guarda una petición en la base de datos interna."""
    request_id = str(uuid.uuid4())
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            'INSERT INTO middleware_requests (id, json_received, emarisma_data) VALUES (?, ?, ?)',
            (request_id, str(json_received), str(emarisma_data) if emarisma_data else None)
        )
        await db.commit()
    return request_id

async def get_request(request_id: str) -> Dict[str, Any]:
    """Obtiene una petición por ID."""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            'SELECT id, json_received, emarisma_data, created_at FROM middleware_requests WHERE id = ?',
            (request_id,)
        )
        row = await cursor.fetchone()
        if row:
            return {
                'id': row[0],
                'json_received': eval(row[1]),
                'emarisma_data': eval(row[2]) if row[2] else None,
                'created_at': row[3]
            }
        return None

async def get_all_requests() -> List[Dict[str, Any]]:
    """Obtiene todas las peticiones."""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('SELECT id, json_received, emarisma_data, created_at FROM middleware_requests')
        rows = await cursor.fetchall()
        return [
            {
                'id': row[0],
                'json_received': eval(row[1]),
                'emarisma_data': eval(row[2]) if row[2] else None,
                'created_at': row[3]
            } for row in rows
        ]

# Inicializar la DB al importar
asyncio.run(init_db())