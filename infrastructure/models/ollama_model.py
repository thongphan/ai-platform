from infrastructure.clients.ollama_client import OllamaClient
from domain.interface.llm_model import Model


class OllamaModel(Model):

    def __init__(self):
        self.client = OllamaClient.get_client()

    def generate(self, prompt: str) -> str:

        response = self.client.chat.completions.create(
            model="llama3",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content