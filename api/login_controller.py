from fastapi import APIRouter, Depends
from domain.models.query_request import QueryRequest
from services.query_service import QueryService
from infrastructure.models.ollama_model import OllamaModel
import  logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/login")
def login(
        request: LoginRequest,

):
    logger.info("Received login request=%s", request.name)



    logger.info("Login processed successfully")

    return {"response": "Login successful"}