from fastapi import FastAPI

from app.database import Base, engine
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CodeCollab AI"
)

@app.get("/")
def root():
    return {
        "message": "CodeCollab AI Backend Running"
    }