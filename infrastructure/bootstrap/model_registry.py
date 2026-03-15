from infrastructure.llm.model_factory import ModelFactory
from infrastructure.llm.ollama_model import OllamaModel
from infrastructure.llm.openai_model import OpenAIModel


def register_models():

    ModelFactory.register("ollama", OllamaModel)
    ModelFactory.register("openai", OpenAIModel)