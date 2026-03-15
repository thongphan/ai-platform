import yaml
from pathlib import Path


class ConfigLoader:

    @staticmethod
    def load(config_path: str):

        file = Path(config_path)

        if not file.exists():
            raise FileNotFoundError(f"Config file not found: {file}")

        with open(file) as f:
            return yaml.safe_load(f)