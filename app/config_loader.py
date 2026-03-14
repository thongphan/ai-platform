import os
import yaml
from pathlib import Path


class ConfigLoader:

    _config = None

    @classmethod
    def load_config(cls):

        if cls._config:
            return cls._config

        config_path = Path("config/config.yaml")

        with open(config_path, "r") as f:
            raw_config = yaml.safe_load(f)

        # detect environment
        env = os.getenv("ENV")

        if not env:
            env = raw_config.get("default_env", "dev")

        if env not in raw_config["environments"]:
            raise ValueError(f"Environment '{env}' not found in config")

        cls._config = raw_config["environments"][env]

        print(f"Loaded configuration for environment: {env}")

        return cls._config


config = ConfigLoader.load_config()