# app.py
import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from routes.routes import router
from config.loader import load_config
from client.risk_client import RiskClient
from middleware.custom_middleware import CustomMiddleware
from services.internal_db_service import init_db
from client_instance import client

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app")

settings = load_config()  # carga config.json o variables de entorno
print("---- APP.PY CARGADO ----")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    logger.info("Base de datos interna inicializada")
    await client.startup()
    logger.info("Cliente HTTP inicializado")
    yield
    # Shutdown
    await client.shutdown()
    logger.info("Cliente HTTP cerrado")

app = FastAPI(title="Risk API Refactorizada", lifespan=lifespan)

# Añade middleware opcional
app.add_middleware(CustomMiddleware, enable_logging=True)

# Incluimos las rutas (usa el router definido)
app.include_router(router)

# Health check endpoint para Docker
@app.get("/health")
async def health_check():
    """Endpoint para verificar que la aplicación está funcionando"""
    return {"status": "healthy", "service": "MiddlewareMarisma"}

# Lifespan events: creamos un RiskClient compartido si quieres, aquí ejemplo de startup/shutdown global
@app.on_event("startup")
async def startup_event():
    logger.info("Arrancando aplicación")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Cerrando aplicación")
