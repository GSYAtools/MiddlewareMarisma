# client/risk_client.py
from typing import Any, Dict, Optional
import httpx
import logging
import base64
import urllib.parse
from config.loader import Settings, load_session_cookies
from urllib.parse import quote_plus

logger = logging.getLogger("risk_client")

class RiskClient:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.base_url = settings.base_url.rstrip("/")
        self._client: Optional[httpx.AsyncClient] = None

    async def startup(self):
        if self._client is None:
            timeout = httpx.Timeout(self.settings.timeout_seconds)
            self._client = httpx.AsyncClient(timeout=timeout)
            logger.info("Httpx AsyncClient inicializado")

    async def shutdown(self):
        if self._client:
            await self._client.aclose()
            self._client = None
            logger.info("Httpx AsyncClient cerrado")

    def _cookie_header(self) -> str:
        cookies = load_session_cookies()
        return "; ".join([f"{k}={v}" for k, v in cookies.items()])

    def _default_headers(self, extra: Dict[str, str] | None = None) -> Dict[str, str]:
        h = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "*/*",
        }
        if extra:
            h.update(extra)
        return h

    async def get(self, path: str, params: Dict[str, Any] | None = None, extra_headers: Dict[str, str] | None = None) -> httpx.Response:
        url = f"{self.base_url}{path}"
        headers = self._default_headers(extra_headers)
        assert self._client is not None, "client not started"
        logger.debug("GET %s params=%s", url, params)
        r = await self._client.get(url, headers=headers, params=params)
        return r

    async def post(self, path: str, content: Any = None, data: Any = None, extra_headers: Dict[str, str] | None = None) -> httpx.Response:
        url = f"{self.base_url}{path}"
        headers = self._default_headers(extra_headers)
        assert self._client is not None, "client not started"
        logger.debug("POST %s data=%s", url, data or content)
        r = await self._client.post(url, headers=headers, content=content, data=data)
        return r

    # Wrappers para acciones del proyecto (ejemplos, adaptables)
    async def exist_user(self) -> httpx.Response:
        path = "/login/existUser"
        cfg = self.settings
        # password_b64 = quote_plus(cfg.password.encode("utf-8").hex())  # nota: mantenemos la codificación original si hace falta
        password_b64 = base64.b64encode(cfg.password.encode("utf-8")).decode("utf-8")
        password_encoded = urllib.parse.quote_plus(password_b64)
        # original used base64+urlencode; adapt as necessary
        content = f"username={cfg.username}&password={password_encoded}"
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "*/*"}
        return await self.post(path, content=content, extra_headers=headers)

    async def authenticate(self) -> httpx.Response:
        path = "/login/authenticate"
        cfg = self.settings
        password_encoded = urllib.parse.quote(cfg.password)
        postUrl = "/login/authenticate"
        content = f"username={cfg.username}&password={password_encoded}&postUrl={postUrl}"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        return await self.post(path, content=content, extra_headers=headers)

    # métodos genéricos para endpoints existentes
    async def cargar_proyectos(self, params: Dict[str, Any] | None = None) -> httpx.Response:
        path = "/proyecto/cargarProyectosTabla/"
        return await self.get(path, params=params)

    async def cargar_subproyectos(self, subproject_id: int, params: Dict[str, Any] | None = None) -> httpx.Response:
        path = f"/subproyecto/cargarSubproyectosTabla/{subproject_id}"
        return await self.get(path, params=params)

    async def guardar_evento(self, content: str) -> httpx.Response:
        path = "/evento/save"


        headers = {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        }
        return await self.post(path, content=content, extra_headers=headers)

    async def obtener_eventos(self, subproyect_id: int, params: Dict[str, Any] | None = None) -> httpx.Response:
        path = f"/evento/cargarEventoTabla/{subproyect_id}"
        return await self.get(path, params=params)
