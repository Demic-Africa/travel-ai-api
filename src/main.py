from fastapi import FastAPI

app = FastAPI(title="Demic Africa Travel AI API")


@app.get("/")
async def root() -> dict[str, str]:
    return {"status": "healthy", "service": "travel-ai-api"}


@app.get("/api/v1/status")
async def api_status() -> dict[str, str]:
    return {"version": "0.1.0", "status": "ok"}
