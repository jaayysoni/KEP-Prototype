from fastapi import APIRouter

from models import ConnectionRequest, StatusResponse, SwitchRequest

router = APIRouter()

# In-memory storage
connections: list[dict] = []
switch_state: str = "ON"


def check_connection(
    from_device: str,
    from_terminal: str,
    to_device: str,
    to_terminal: str,
) -> bool:
    """Check if a specific connection exists."""
    for connection in connections:
        if (
            connection["from_device"] == from_device
            and connection["from_terminal"] == from_terminal
            and connection["to_device"] == to_device
            and connection["to_terminal"] == to_terminal
        ):
            return True
    return False


def is_led_on() -> bool:
    """Determine whether the LED should be ON or OFF."""
    pos_connected = check_connection(
        "battery", "positive", "led", "positive"
    )
    neg_connected = check_connection(
        "battery", "negative", "led", "negative"
    )

    if not (pos_connected and neg_connected):
        return False

    if switch_state == "OFF":
        return False

    return True


@router.get("/status", response_model=StatusResponse)
def get_status() -> StatusResponse:
    """Get current LED and switch status."""
    led_on = is_led_on()

    return StatusResponse(
        led_status="ON" if led_on else "OFF",
        switch=switch_state,
        valid_circuit=led_on,
    )


@router.post("/connect")
def connect(request: ConnectionRequest) -> dict:
    """Create a connection between two device terminals."""

    data = request.model_dump()

    # Prevent invalid connection (same device)
    if request.from_device == request.to_device:
        return {"error": "Cannot connect same device"}

    # Prevent duplicate connection
    if data in connections:
        return {"message": "Connection already exists"}

    connections.append(data)

    return {
        "message": "Connected successfully",
        "total_connections": len(connections),
    }


@router.post("/disconnect")
def disconnect() -> dict:
    """Clear all connections."""
    connections.clear()

    return {"message": "All connections cleared"}


@router.post("/switch")
def toggle_switch(request: SwitchRequest) -> dict:
    """Update switch state."""
    global switch_state
    switch_state = request.state

    return {
        "message": "Switch updated",
        "switch": switch_state,
    }