from sqlalchemy import Column,Integer,String
from app.db.base import Base
from sqlalchemy.orm import relationship

class Permission(Base):

    __tablename__ = "sys_permission"

    id = Column(Integer, primary_key=True)

    name = Column(String(50))

    code = Column(String(100), unique=True)

    type = Column(Integer)

    roles = relationship(
        "Role",
        secondary="sys_role_permission",
        back_populates="permissions"
    )