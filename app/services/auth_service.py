from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token


def register_user(db: Session, email: str, name: str, password: str):
    print('查看用户名',email,name,password)
    user = User(
        email=email,
        name=name,
        password=hash_password(password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

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