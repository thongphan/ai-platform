class ModelFactory:

    _registry = {}

    @classmethod
    def register(cls, provider: str, model_cls):

        cls._registry[provider] = model_cls

    @classmethod
    def create(cls, settings):

        provider = settings.llm.provider

        if provider not in cls._registry:
            raise ValueError(f"Unsupported provider {provider}")

        model_cls = cls._registry[provider]

        return model_cls(
            base_url=settings.llm.base_url,
            api_key=settings.llm.api_key,
            model=settings.llm.model
        )