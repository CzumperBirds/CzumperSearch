"""Model for the control request."""

from pydantic import BaseModel
from enum import Enum


class Action(str, Enum):
    """Enum for controlling producers."""

    start = "start"
    stop = "stop"


class ControlRequest(BaseModel):
    """Request to control the producers."""

    action: Action
