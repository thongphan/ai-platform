from abc import ABC, abstractmethod


class LLMModel(ABC):
    """
    Abstract model interface.
    All LLM providers must implement this contract.
    """

    @abstractmethod
    async def generate(self, prompt: str) -> str:
        pass

    @abstractmethod
    async def generate_stream(self, prompt: str):
        pass