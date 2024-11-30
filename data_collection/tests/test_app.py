"""Module for testing the FastAPI app."""

from unittest.mock import patch
import pytest
from fastapi.testclient import TestClient
from src.app import app
from src.model.api import Action
import src.config

client = TestClient(app=app)


@pytest.fixture(autouse=True)
def reset_running_flag():
    """Ensure RUNNING flag is reset to False before each test."""
    src.config.RUNNING = False
    yield
    src.config.RUNNING = False


def test_control_producers_start():
    """Test the control_producers endpoint with START action."""
    with patch("src.utils.producer_manager.start_producers") as mock_start_producers:
        response = client.post(
            "/api/v1/data-collection/control", json={"action": Action.START.value}
        )
        assert response.status_code == 200
        assert response.json() == {"is_running": True}


def test_control_producers_stop():
    """Test the control_producers endpoint with STOP action."""
    with patch("src.utils.producer_manager.stop_producers") as mock_stop_producers:
        src.config.RUNNING = True
        response = client.post(
            "/api/v1/data-collection/control", json={"action": Action.STOP.value}
        )
        assert response.status_code == 200
        assert response.json() == {"is_running": False}


def test_get_status():
    """Test the get_status endpoint."""
    response = client.get("/api/v1/data-collection/status")
    assert response.status_code == 200
    assert response.json() == {"is_running": src.config.RUNNING}
