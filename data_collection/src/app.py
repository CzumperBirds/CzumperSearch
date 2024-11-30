"""Main application file to control the producers."""

from fastapi import FastAPI, APIRouter
from src.model.control_request import Action, ControlRequest
from src.utils.producer_manager import start_producers, stop_producers
import src.config

app = FastAPI()
router = APIRouter(prefix="/api/v1/data-collection")


@router.post("/control")
async def control_producers(request: ControlRequest):
    """Control the start or stop of the producers."""
    match request.action:
        case Action.start:
            start_producers()

        case Action.stop:
            stop_producers()

    return {"is_running": src.config.RUNNING}


@router.get("/status")
async def get_status():
    """Return status of service"""
    return {"is_running": src.config.RUNNING}


app.include_router(router)
