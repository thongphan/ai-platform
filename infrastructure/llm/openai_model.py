import time
import logging

from openai import OpenAI
from domain.abstraction.llm_model import LLMModel

logger = logging.getLogger(__name__)


class OpenAIModel(LLMModel):

    def __init__(self, base_url: str, model: str, api_key: str):

        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key,
            timeout=120.0
        )

        self.model = model

    def generate(self, prompt: str) -> str:

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant"},
                {"role": "user", "content": prompt}
            ],
        )

        if not response.choices:
            raise RuntimeError("Model returned empty response")

        content = response.choices[0].message.content

        return content.strip() if content else ""

    def generate_stream(self, prompt: str):

        retries = 3

        for attempt in range(retries):

            try:

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

                return

            except Exception as ex:

                logger.warning(
                    "Streaming attempt %s failed: %s",
                    attempt + 1,
                    ex
                )

                if attempt < retries - 1:
                    time.sleep(2)
                else:
                    logger.exception("LLM streaming failed after retries")
                    raise RuntimeError("LLM request failed") from ex