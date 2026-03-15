from functools import lru_cache

from application.prompt.prompt_builder import PromptBuilder
from infrastructure.config.settings_provider import SettingsProvider
from infrastructure.llm.model_factory import ModelFactory

from application.services.query_services.query_service import QueryService


@lru_cache()
def get_model():

    settings = SettingsProvider.get_settings()

    return ModelFactory.create(settings)


def get_query_service():
    model = get_model()
    prompt_builder = PromptBuilder()

    return QueryService(model, prompt_builder)