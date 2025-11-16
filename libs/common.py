import json
from pathlib import Path
from typing import Any, Dict


def json_reader(file_name: str, file_path: Path) -> Dict[str, Any]:
    """Read and return JSON contents from the given path.

    Args:
        file_name: name of json file
        file_path: Path to the folder containing the file

    Returns:
        Parsed JSON as dict

    Raises:
        FileNotFoundError: if file does not exist
    """
    full_path = file_path / file_name
    try:
        with full_path.open("r", encoding="utf-8") as json_data:
            return json.load(json_data)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"File not found: {full_path}") from exc


def load_device_config(platform: str, base_path: Path = Path.cwd()) -> Dict[str, Any]:
    resources = base_path / "resources"
    config_data = json_reader(file_name="desired_capabilities.json", file_path=resources)
    if platform.lower() not in ("android", "ios"):
        raise ValueError(f"No such platform: {platform}")
    return config_data[platform]


def load_user_data(base_path: Path = Path.cwd()) -> Dict[str, Any]:
    data = base_path / "data"
    return json_reader(file_name="users.json", file_path=data)
