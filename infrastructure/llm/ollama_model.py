from openai import OpenAI
from domain.abstraction.llm_model import LLMModel


class OllamaModel(LLMModel):

    def __init__(self, base_url: str, model: str, api_key: str):

        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key
        )

        self.model = model

    def generate(self, prompt: str) -> str:

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant"},
                {"role": "user", "content": prompt}
            ]
        )

        if not response.choices:
            raise RuntimeError("Model returned empty response")

        return response.choices[0].message.content.strip()

    def generate_stream(self, prompt: str):

        stream = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant"},
                {"role": "user", "content": prompt}
            ],
            stream=True
        )

        for chunk in stream:

            delta = chunk.choices[0].delta

            if delta and delta.content:
                yield delta.content