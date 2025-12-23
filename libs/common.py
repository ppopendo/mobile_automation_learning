import json
from pathlib import Path
from typing import Any, Dict


def json_reader(file_name: str, file_path: str) -> Dict[str, Any]:
    """Read and return JSON contents from the given path.

    Args:
        file_name: name of json file
        file_path: Path to the folder containing the file

    Returns:
        Parsed JSON as dict

    Raises:
        FileNotFoundError: if file does not exist
    """
    try:
        with open(f"{file_path}/{file_name}", "r", encoding="utf-8") as json_data:
            return json.load(json_data)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"File not found: {file_path}/{file_name}") from exc


def load_device_capabilities(platform: str, app_name: str) -> Dict[str, Any]:
    if platform.lower() not in ("android", "ios"):
        raise ValueError(f"No such platform: {platform}")
    config_data = json_reader(file_name=f"{platform}_capabilities.json", file_path=f"{Path.cwd()}/resources/{app_name}")
    return config_data


def load_user_data() -> Dict[str, Any]:
    return json_reader(file_name="users.json", file_path=f"{Path.cwd()}/data")
