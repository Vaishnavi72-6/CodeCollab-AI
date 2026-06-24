from fastapi import FastAPI

app = FastAPI(
    title="CodeCollab AI",
    description="Real-Time Collaborative Code Editor Backend",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to CodeCollab AI Backend"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }