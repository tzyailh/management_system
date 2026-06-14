from sqlalchemy import Column,Integer,String
from app.db.base import Base

class Menu(Base):

    __tablename__ = "sys_menu"

    id = Column(Integer, primary_key=True)

    parent_id = Column(Integer)

    title = Column(String(50))

    path = Column(String(100))

    component = Column(String(200))

    icon = Column(String(50))

    permission = Column(String(100))