from sqlalchemy import Column, Integer, String
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    name = Column(String(50))
    password = Column(String(255))

    # 权限字段
    role = Column(String(20), default="user")  # admin / user