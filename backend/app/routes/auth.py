from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.database import get_db
from app.models.user import User
from app.schemas.user_schema import UserRegister
from app.auth.hashing import hash_password
from app.auth.hashing import verify_password
from app.auth.jwt_handler import create_access_token
from app.schemas.user_schema import UserLogin
from app.dependencies.auth import get_current_user
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        return {
            "message": "Email already registered"
        }

    new_user = User(
        name=user.name,
        email=user.email,
        password_hash=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    db_user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if not db_user:
        return {
            "message": "Invalid email"
        }

    if not verify_password(
        form_data.password,
        db_user.password_hash
    ):
        return {
            "message": "Invalid password"
        }

    token = create_access_token(
        {
            "sub": db_user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
@router.get("/me")
def current_user(
    user: User = Depends(get_current_user)
):

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }