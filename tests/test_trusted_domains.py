import json
import pytest

from bhram.rules import load_trusted_domains


@pytest.fixture(autouse=True)
def clear_cache():
    load_trusted_domains.cache_clear()
    yield
    load_trusted_domains.cache_clear()


def create_data_file(tmp_path, content):
    data_dir = tmp_path / "data"
    data_dir.mkdir(exist_ok=True)

    file_path = data_dir / "trusted_domains.json"
    file_path.write_text(content, encoding="utf-8")


def test_load_trusted_domains(tmp_path, monkeypatch):
    data = {
        "payments": [
            "https://esewa.com.np",
            "https://khalti.com"
        ]
    }

    create_data_file(tmp_path, json.dumps(data))
    monkeypatch.chdir(tmp_path)

    result = load_trusted_domains()

    assert result == ["esewa.com.np", "khalti.com"]


def test_load_nested_trusted_domains(tmp_path, monkeypatch):
    data = {
        "payments": {
            "wallets": [
                "https://esewa.com.np"
            ]
        },
        "banks": [
            "https://nabilbank.com"
        ]
    }

    create_data_file(tmp_path, json.dumps(data))
    monkeypatch.chdir(tmp_path)

    result = load_trusted_domains()

    assert result == ["esewa.com.np", "nabilbank.com"]


def test_missing_trusted_domains_file(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)

    result = load_trusted_domains()

    assert result == []
    assert "file was not found" in capsys.readouterr().out


def test_invalid_trusted_domains_json(tmp_path, monkeypatch, capsys):
    create_data_file(tmp_path, "{invalid json}")
    monkeypatch.chdir(tmp_path)

    result = load_trusted_domains()

    assert result == []
    assert "JSON file is invalid" in capsys.readouterr().out


def test_unexpected_json_structure(tmp_path, monkeypatch):
    data = ["https://esewa.com.np", "https://khalti.com"]

    create_data_file(tmp_path, json.dumps(data))
    monkeypatch.chdir(tmp_path)

    result = load_trusted_domains()

    assert result == []


def test_trusted_domains_file_access_error(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)

    def fake_open(*args, **kwargs):
        raise PermissionError("Permission denied")

    monkeypatch.setattr("builtins.open", fake_open)

    result = load_trusted_domains()

    assert result == []
    assert "Error loading trusted domains" in capsys.readouterr().out


def test_trusted_domains_cache(tmp_path, monkeypatch):
    first_data = {
        "payments": ["https://esewa.com.np"]
    }

    create_data_file(tmp_path, json.dumps(first_data))
    monkeypatch.chdir(tmp_path)

    first_result = load_trusted_domains()

    second_data = {
        "payments": ["https://khalti.com"]
    }

    create_data_file(tmp_path, json.dumps(second_data))

    cached_result = load_trusted_domains()

    assert first_result == ["esewa.com.np"]
    assert cached_result == ["esewa.com.np"]

    load_trusted_domains.cache_clear()

    updated_result = load_trusted_domains()

    assert updated_result == ["khalti.com"]
