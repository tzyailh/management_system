# 用户角色关联表

from sqlalchemy import Column,Integer,ForeignKey
from app.db.base import Base

class UserRole(Base):

    __tablename__ = "sys_user_role"

    user_id = Column(
        "user_id",
        ForeignKey("sys_user.id"),
        primary_key=True
    )

    role_id = Column(
        "role_id",
        ForeignKey("sys_role.id"),
        primary_key=True
    )