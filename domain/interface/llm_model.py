from abc import ABC, abstractmethod


class Model(ABC):
    """
    Abstract model interface.
    All LLM providers must implement this contract.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass