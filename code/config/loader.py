# config/loader.py
from pathlib import Path
from typing import Dict, Any
from pydantic_settings import BaseSettings
import json

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    base_url: str = "http://172.20.48.129:8090"
    username: str = ""
    password: str = ""
    timeout_seconds: int = 30
    new_event: Dict[str, Any] = {}
    new_gravedad: Dict[str, Any] = {}
    new_amenaza: Dict[str, Any] = {}

    class Config:
        env_prefix = "RISK_"
        env_file = ".env",
        extra = "allow"

def load_config(path: str | None = None) -> Settings:
    """
    Carga la configuración desde config.json si existe, sino usa variables de entorno.
    """
    settings = Settings()
    config_path = Path(path) if path else BASE_DIR / "config.json"
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        # merge into Settings
        settings = Settings(**{**settings.model_dump(), **data})
    return settings

def load_session_cookies(path: str | None = None) -> Dict[str, str]:
    session_path = Path(path) if path else BASE_DIR.parent / "session.json"
    if session_path.exists():
        with open(session_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}
