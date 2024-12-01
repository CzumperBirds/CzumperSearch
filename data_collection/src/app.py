"""Main application file to control the producers."""

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from src.model.api import Action, ControlRequest, StatusResponse
from src.utils.producer_manager import start_producers, stop_producers
import src.config

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://search-test.czumpers.com",
        "https://search.czumpers.com",
        "http://localhost:4200",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(prefix="/api/v1/data-collection")


@router.post("/control")
async def control_producers(request: ControlRequest) -> StatusResponse:
    """Control the start or stop of the producers."""
    match request.action:
        case Action.START:
            start_producers()

        case Action.STOP:
            stop_producers()

    return StatusResponse(is_running=src.config.RUNNING)


@router.get("/status")
async def get_status() -> StatusResponse:
    """Return status of service"""
    return StatusResponse(is_running=src.config.RUNNING)


app.include_router(router)
