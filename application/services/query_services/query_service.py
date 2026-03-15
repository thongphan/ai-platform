import logging

from domain.abstraction.llm_model import LLMModel
from domain.models.query_schema.query_request import QueryRequest

logger = logging.getLogger(__name__)


class QueryService:

    def __init__(self, model: LLMModel, prompt_builder):
        self.model = model
        self.prompt_builder = prompt_builder

    def handle_query(self, request: QueryRequest) :

        prompt = self.prompt_builder.build(request)

        logger.info(
            "Calling LLM model=%s for user=%s",
            type(self.model).__name__,
            request.name
        )

        try:

            response = self.model.generate(prompt)

            logger.info("LLM response generated successfully")

            return response

        except Exception:

            logger.exception("LLM generation failed")

            raise

    def stream_query(self, request: QueryRequest):

        prompt = self.prompt_builder.build(request)

        logger.info(
            "Streaming response from model=%s",
            type(self.model).__name__
        )

        return self.model.generate_stream(prompt)