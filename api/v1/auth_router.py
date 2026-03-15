from fastapi import APIRouter
from domain.models.input_schema.LoginRequest import LoginRequest
import  logging

logger = logging.getLogger(__name__)
router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(request: LoginRequest):

    logger.info("Received login request=%s", request.name)

    return {"response": "Login successful"}