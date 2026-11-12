import os

from src.app import root


def test_root_default_version(monkeypatch):
    monkeypatch.delenv("APP_VERSION", raising=False)

    response = root()

    assert response == {
        "status": "ok",
        "version": "dev"
    }


def test_root_custom_version(monkeypatch):
    monkeypatch.setenv("APP_VERSION", "v1.0.0")

    response = root()

    assert response == {
        "status": "ok",
        "version": "v1.0.0"
    }
