# middleware/custom_middleware.py
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response
import time
import logging

logger = logging.getLogger("middleware")

class CustomMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, enable_logging: bool = True):
        super().__init__(app)
        self.enable_logging = enable_logging

    async def dispatch(self, request: Request, call_next):
        start = time.time()
        if self.enable_logging:
            logger.info(f"→ {request.method} {request.url.path}")
        response: Response = await call_next(request)
        if self.enable_logging:
            elapsed = (time.time() - start) * 1000
            logger.info(f"← {request.method} {request.url.path} {response.status_code} ({elapsed:.2f}ms)")
        return response
