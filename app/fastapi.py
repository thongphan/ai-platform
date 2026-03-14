import logging

from fastapi import FastAPI
from app.config_loader import config

from middleware.request_logger import log_requests
import uvicorn
from api.query_controller import router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)

app = FastAPI(title=config["app"]["name"])

app.middleware("http")(log_requests)
app.include_router(router)

logger.info("FastAPI application started")
if __name__ == '__main__':
    uvicorn.run(
        "rag_practice_coursesa.fastapi:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )