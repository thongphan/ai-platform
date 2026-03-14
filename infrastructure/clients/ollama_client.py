from openai import OpenAI
from app.config_loader import config

class OllamaClient:
    """
    Singleton client to reuse connection across services.
    """

    _client = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            cls._client = OpenAI(
                base_url=config["llm"]["base_url"],
                api_key=config["llm"]["api_key"]
            )
        return cls._client