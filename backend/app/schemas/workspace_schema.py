from pydantic import BaseModel

class WorkspaceCreate(BaseModel):
    name: str
    description: str

class WorkspaceResponse(BaseModel):
    id: str
    name: str
    description: str
    owner_id: str

    class Config:
        from_attributes = True