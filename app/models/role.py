from sqlalchemy import Column, Integer, String
from app.db.base import Base
from sqlalchemy.orm import relationship

class Role(Base):
    __tablename__ = "sys_role"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    code = Column(String(50), unique=True)
    remark = Column(String(200))
    users = relationship(
        "User",
        secondary="sys_user_role",
        back_populates="roles"
    )

    permissions = relationship(
        "Permission",
        secondary="sys_role_permission",
        back_populates="roles"
    )