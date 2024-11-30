"""Main application file to control the producers."""

from fastapi import FastAPI
from src.model.control_request import ControlRequest
from src.utils.producer_manager import start_producers, stop_producers

app = FastAPI()


@app.post("/control")
async def control_producers(request: ControlRequest) -> tuple[dict, int]:
    """Control the start or stop of the producers."""
    if request.action == "start":
        start_producers()
        return {"status": "Producers started"}, 200

    if request.action == "stop":
        stop_producers()
        return {"status": "Producers stopped"}, 200

    return {"status": "Invalid action"}, 400
