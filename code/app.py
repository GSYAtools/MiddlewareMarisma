# app.py
import logging
from fastapi import FastAPI
from routes.step_routes import router
from config.loader import load_config
from client.risk_client import RiskClient
from middleware.custom_middleware import CustomMiddleware

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app")

settings = load_config()  # carga config.json o variables de entorno
print("---- APP.PY CARGADO ----")
app = FastAPI(title="Risk API Refactorizada")

# Añade middleware opcional
app.add_middleware(CustomMiddleware, enable_logging=True)

# Incluimos las rutas (usa el router definido)
app.include_router(router)

# Lifespan events: creamos un RiskClient compartido si quieres, aquí ejemplo de startup/shutdown global
@app.on_event("startup")
async def startup_event():
    logger.info("Arrancando aplicación")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Cerrando aplicación")
