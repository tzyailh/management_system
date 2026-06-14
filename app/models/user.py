from sqlalchemy import Column, Integer, String
from app.db.base import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "sys_user"

    id = Column(Integer, primary_key=True)

    username = Column(String(50))

    roles = relationship(
        "Role",
        secondary="sys_user_role",
        back_populates="users"
    )