from typing import Literal

from pydantic import BaseModel


# Type aliases (PEP 8: uppercase for constants/types)
DeviceType = Literal["battery", "led"]
TerminalType = Literal["positive", "negative"]
SwitchState = Literal["ON", "OFF"]


class ConnectionRequest(BaseModel):
    """Request model for connecting two device terminals."""

    from_device: DeviceType
    from_terminal: TerminalType
    to_device: DeviceType
    to_terminal: TerminalType


class SwitchRequest(BaseModel):
    """Request model for toggling switch state."""

    state: SwitchState


class StatusResponse(BaseModel):
    """Response model for LED status."""

    led_status: SwitchState
    switch: SwitchState
    valid_circuit: bool