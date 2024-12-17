"""Main application file to control the producers."""

from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from src.model.api import Action, ControlRequest, StatusResponse
from src.utils.producer_manager import init_producers, start_producers, pause_producers
import src.config


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Start and stop producers when the application starts and stops."""
    try:
        init_producers()
        yield
    finally:
        pause_producers()


app = FastAPI(lifespan=lifespan)

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
            pause_producers()

    return StatusResponse(is_running=src.config.RUNNING)


@router.get("/status")
async def get_status() -> StatusResponse:
    """Return status of service"""
    return StatusResponse(is_running=src.config.RUNNING)


app.include_router(router)
