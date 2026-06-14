from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token


def register_user(db: Session, username: str, name: str, password: str):
    user = User(
        username=username,
        name=name,
        password=hash_password(password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return user


def login_user(user: User):
    token = create_access_token(
        data={"sub": str(user.id), "role": user.role}
    )
    return token

def get_current_permissions(user):

    permissions = set()

    for role in user.roles:
        for p in role.permissions:
            permissions.add(p.code)

    return permissions