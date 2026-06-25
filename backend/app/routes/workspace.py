from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.workspace import Workspace
from app.schemas.workspace_schema import WorkspaceCreate
from app.dependencies.auth import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/workspace",
    tags=["Workspace"]
)

@router.post("/create")
def create_workspace(
    workspace: WorkspaceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_workspace = Workspace(
        name=workspace.name,
        description=workspace.description,
        owner_id=current_user.id
    )

    db.add(new_workspace)
    db.commit()
    db.refresh(new_workspace)

    return {
        "message": "Workspace created successfully",
        "workspace_id": new_workspace.id
    }
@router.get("/all")
def get_all_workspaces(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    workspaces = db.query(Workspace).filter(
        Workspace.owner_id == current_user.id
    ).all()

    return workspaces