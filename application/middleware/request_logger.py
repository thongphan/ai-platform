import logging
import time
from fastapi import Request

logger = logging.getLogger("api")


async def log_requests(request: Request, call_next):

    start_time = time.time()

    logger.info("Request started: %s %s", request.method, request.url)

    response = await call_next(request)

    duration = time.time() - start_time

    logger.info(
        "Request completed: status=%s duration=%.3fs",
        response.status_code,
        duration
    )

    return response