"""Model for the control request."""

from enum import Enum
from pydantic import BaseModel


class Action(str, Enum):
    """Enum for controlling producers."""

    START = "start"
    STOP = "stop"


class ControlRequest(BaseModel):
    """Request to control the producers."""

    action: Action


class StatusResponse(BaseModel):
    """Response for the status of the producers."""

    is_running: bool
