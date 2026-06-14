from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse
from app.services.auth_service import register_user, authenticate_user, login_user
from app.db.session import get_db
from app.api.deps import get_current_user, require_admin, permission_required
from app.models.user import User

router = APIRouter()


@router.post("/register")
def register(req: RegisterRequest, db: Session = Depends(get_db)):
    return register_user(db, req.username, req.name, req.password)


@router.post("/login", response_model=TokenResponse)
def login(req: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, req.username, req.password)

    if not user:
        return {"error": "Invalid credentials"}

    token = login_user(user)

    return {"access_token": token}


@router.post("/me")
def me(user: User = Depends(get_current_user)):
    return user


@router.get("/admin")
def admin_route(user: User = Depends(require_admin)):
    return {"msg": "Welcome admin"}

@router.get(
    "/list",
    dependencies=[
        Depends(
            permission_required(
                "user:list"
            )
        )
    ]
)
async def user_list():
    pass

@router.delete(
    "/{user_id}",
    dependencies=[
        Depends(
            permission_required(
                "user:delete"
            )
        )
    ]
)
async def delete_user():
    pass