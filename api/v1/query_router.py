from fastapi import APIRouter, Depends
import logging

from domain.models.query_schema.query_request import QueryRequest
from application.services.query_services.query_service import QueryService
from infrastructure.dependency.providers import get_query_service
from fastapi.responses import StreamingResponse
logger = logging.getLogger(__name__)

router = APIRouter(tags=["Query"])


@router.post("/query")
def query(
        request: QueryRequest,
        service: QueryService = Depends(get_query_service)
):

    logger.info("Received query from user=%s", request.name)

    result = service.handle_query(request)

    logger.info("Query processed successfully")

    return {"response": result}

@router.post("/query-stream")
def query_stream(request: QueryRequest, service=Depends(get_query_service)):

    return StreamingResponse(
        service.stream_query(request),
        media_type="text/plain"
    )