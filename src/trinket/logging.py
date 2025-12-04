import logging.config
from pathlib import Path
from typing import Any

import yaml

from .path import find_upwards


class YamlConfig:

    def __init__(self, file_name: str) -> None:

        config_path = find_upwards(file_name)
        if config_path is None:
            raise FileNotFoundError(f"logging config file `{file_name}` not found")

        self.file_name = file_name
        self.config_path = config_path

        self.config = self._load(config_path)

    @staticmethod
    def _load(config_path: Path) -> Any:
        return yaml.safe_load(config_path.read_text())

    def config_logging(self) -> None:
        logging.config.dictConfig(self.config)
