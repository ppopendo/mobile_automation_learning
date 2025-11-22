from pathlib import Path
from libs.common import json_reader, load_user_data


def test_json_reader_reads_file(tmp_path: Path):
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    file_path = data_dir / "users.json"
    content = '{"valid_users": [{"username": "a", "password": "b"}]}'
    file_path.write_text(content, encoding="utf-8")

    result = json_reader(file_name="users.json", file_path=data_dir)
    assert "valid_users" in result


def test_load_user_data_uses_default(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    file_path = data_dir / "users.json"
    file_path.write_text('{"valid_users": []}', encoding="utf-8")

    result = load_user_data()
    assert isinstance(result, dict)
