"""Model for the control request."""

from pydantic import BaseModel


class ControlRequest(BaseModel):
    """Request to control the producers."""

    action: str
