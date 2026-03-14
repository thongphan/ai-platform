from domain.interface.llm_model import Model
from domain.models.query_request import QueryRequest
import logging

logger = logging.getLogger(__name__)

class QueryService:

    def __init__(self, model: Model):
        self.model = model

    def handle_query(self, request: QueryRequest) -> str:
        logger.info("Building prompt")

        prompt = f"""
        User: {request.name}
        Question: {request.query}
        """

        logger.info("Calling LLM model")

        try:
            response = self.model.generate(prompt)
            logger.info(f"LLM response received {response}")
            return response
        except Exception as e:
            logger.exception("LLM generation failed")
            raise

    def _build_prompt(self, request: QueryRequest):

        return f"""
User: {request.name}

Question:
{request.query}
"""