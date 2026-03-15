import os
import logging

from domain.models.app_settings import Settings
from .config_loader import ConfigLoader
from .runtime_detector import RuntimeDetector

logger = logging.getLogger(__name__)


class SettingsProvider:

    _settings: Settings | None = None

    @classmethod
    def get_settings(cls) -> Settings:

        if cls._settings:
            return cls._settings

        env = os.getenv("ENV")

        if not env:
            env = RuntimeDetector.detect()

        if not env:
            env = "dev"

        config_path = f"config/{env}.yaml"

        raw = ConfigLoader.load(config_path)

        cls._settings = Settings(**raw)

        logger.info("Loaded configuration for environment: %s", env)

        return cls._settings

    @classmethod
    def reset(cls):
        cls._settings = None