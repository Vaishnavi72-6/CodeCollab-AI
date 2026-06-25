from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.workspace import Workspace
from app.schemas.workspace_schema import WorkspaceCreate
from app.dependencies.auth import get_current_user
from app.models.user import User
from fastapi import HTTPException
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
@router.get("/{workspace_id}")
def get_workspace(
    workspace_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    workspace = db.query(Workspace).filter(
        Workspace.id == workspace_id,
        Workspace.owner_id == current_user.id
    ).first()

    if not workspace:
        raise HTTPException(
            status_code=404,
            detail="Workspace not found"
        )

    return workspace
@router.put("/update/{workspace_id}")
def update_workspace(
    workspace_id: str,
    workspace: WorkspaceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    db_workspace = db.query(Workspace).filter(
        Workspace.id == workspace_id,
        Workspace.owner_id == current_user.id
    ).first()

    if not db_workspace:
        raise HTTPException(
            status_code=404,
            detail="Workspace not found"
        )

    db_workspace.name = workspace.name
    db_workspace.description = workspace.description

    db.commit()
    db.refresh(db_workspace)

    return {
        "message": "Workspace updated successfully",
        "workspace": db_workspace
    }
@router.delete("/delete/{workspace_id}")
def delete_workspace(
    workspace_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    workspace = db.query(Workspace).filter(
        Workspace.id == workspace_id,
        Workspace.owner_id == current_user.id
    ).first()

    if not workspace:
        raise HTTPException(
            status_code=404,
            detail="Workspace not found"
        )

    db.delete(workspace)
    db.commit()

    return {
        "message": "Workspace deleted successfully"
    }