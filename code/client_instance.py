# client_instance.py
from config.loader import load_config
from client.risk_client import RiskClient

settings = load_config()
client = RiskClient(settings)