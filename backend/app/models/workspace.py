from sqlalchemy import Column, String, DateTime
from app.database import Base
import uuid
from datetime import datetime

class Workspace(Base):
    __tablename__ = "workspaces"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    name = Column(
        String,
        nullable=False
    )

    description = Column(
        String
    )

    owner_id = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )