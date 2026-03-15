import logging
import uvicorn

from fastapi import FastAPI

from application.middleware.request_logger import log_requests
from infrastructure.config.settings_provider import SettingsProvider
from infrastructure.bootstrap.model_registry import register_models
from api.v1.router import router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)

settings = SettingsProvider.get_settings()

app = FastAPI(title=settings.app.name)

app.middleware("http")(log_requests)

@app.on_event("startup")
def startup():
    register_models()

app.include_router(router)

@app.get("/")
def health():
    return {
        "app": settings.app.name,
        "llm_endpoint": settings.llm.base_url
    }


if __name__ == "__main__":
    logger.info("FastAPI application started")

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )