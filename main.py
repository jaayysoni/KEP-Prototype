from fastapi import FastAPI

from routers.device import router


app = FastAPI(
    title="IoT Simulator API",
    description=(
        "Simulates battery, LED, and switch connections using FastAPI"
    ),
    version="1.0.0",
)


app.include_router(
    router,
    prefix="/api",
    tags=["IoT Simulator"],
)


@app.get("/")
def root() -> dict:
    """Root endpoint to verify the API is running."""
    return {
        "message": "IoT Simulator is running 🚀",
        "docs": "http://127.0.0.1:8000/docs",
    }


@app.get("/health")
def health() -> dict:
    """Health check endpoint."""
    return {
        "status": "OK",
        "service": "IoT Simulator",
    }