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
        # Asegurar UTF-8 (aunque es por defecto en SQLite moderno)
        await db.execute("PRAGMA encoding = 'UTF-8'")
        # Establecer versión de la DB
        await db.execute("PRAGMA user_version = 1")
        # Crear tablas necesarias
        await db.execute('''
            CREATE TABLE IF NOT EXISTS middleware_requests (
                id TEXT PRIMARY KEY,
                json_received TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS emarisma_data (
                request_id TEXT PRIMARY KEY,
                data TEXT,
                FOREIGN KEY (request_id) REFERENCES middleware_requests (id)
            )
        ''')
        await db.commit()

async def save_request(json_received: Dict[str, Any], emarisma_data: Dict[str, Any] = None) -> str:
    """Guarda una petición en la base de datos interna."""
    request_id = str(uuid.uuid4())
    async with aiosqlite.connect(DB_PATH) as db:
        # Insertar en middleware_requests
        await db.execute(
            'INSERT INTO middleware_requests (id, json_received) VALUES (?, ?)',
            (request_id, str(json_received))
        )
        # Insertar o reemplazar en emarisma_data si hay datos
        if emarisma_data:
            await db.execute(
                'INSERT OR REPLACE INTO emarisma_data (request_id, data) VALUES (?, ?)',
                (request_id, str(emarisma_data))
            )
        await db.commit()
    return request_id

async def update_emarisma_data(request_id: str, emarisma_data: Dict[str, Any]):
    """Actualiza los datos asociados de eMarisma para una petición."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            'INSERT OR REPLACE INTO emarisma_data (request_id, data) VALUES (?, ?)',
            (request_id, str(emarisma_data))
        )
        await db.commit()

async def get_request(request_id: str) -> Dict[str, Any]:
    """Obtiene una petición por ID con sus datos asociados."""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('''
            SELECT r.id, r.json_received, r.created_at, e.data
            FROM middleware_requests r
            LEFT JOIN emarisma_data e ON r.id = e.request_id
            WHERE r.id = ?
        ''', (request_id,))
        row = await cursor.fetchone()
        if row:
            return {
                'id': row[0],
                'json_received': eval(row[1]),
                'created_at': row[2],
                'emarisma_data': eval(row[3]) if row[3] else None
            }
        return None

async def get_all_requests() -> List[Dict[str, Any]]:
    """Obtiene todas las peticiones con sus datos asociados."""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('''
            SELECT r.id, r.json_received, r.created_at, e.data
            FROM middleware_requests r
            LEFT JOIN emarisma_data e ON r.id = e.request_id
        ''')
        rows = await cursor.fetchall()
        return [
            {
                'id': row[0],
                'json_received': eval(row[1]),
                'created_at': row[2],
                'emarisma_data': eval(row[3]) if row[3] else None
            } for row in rows
        ]

# Inicializar la DB al importar (solo para desarrollo; en producción, llamar init_db() en startup)
# asyncio.run(init_db())  # Comentado para evitar ejecución automática