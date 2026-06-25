from fastapi import FastAPI
from app.models.workspace import Workspace
from app.routes.workspace import router as workspace_router
from app.database import Base, engine
from app.models.user import User
from app.routes.auth import router as auth_router
from app.models.user import User
from app.models.workspace import Workspace


Base.metadata.create_all(bind=engine)

app = FastAPI(title="CodeCollab AI")

app.include_router(auth_router)
app.include_router(workspace_router)
@app.get("/")
def root():
    return {
        "message": "CodeCollab AI Backend Running"
    }