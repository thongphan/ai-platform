from fastapi import APIRouter, Depends
from domain.models.query_request import QueryRequest
from services.query_service import QueryService
from infrastructure.models.ollama_model import OllamaModel
import  logging

logger = logging.getLogger(__name__)
router = APIRouter()


def get_query_service():

    model = OllamaModel()

    return QueryService(model)


@router.post("/query")
def query(
        request: QueryRequest,
        service: QueryService = Depends(get_query_service)
):
    logger.info("Received query from user=%s", request.name)

    result = service.handle_query(request)

    logger.info("Query processed successfully")

    return {"response": result}