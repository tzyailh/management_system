# 角色权限关联表

from sqlalchemy import Column,Integer,ForeignKey
from app.db.base import Base

class RolePermission(Base):

    __tablename__ = "sys_role_permission"

    role_id = Column(
        'role_id',
        ForeignKey("sys_role.id"),
        primary_key=True
    )

    permission_id = Column(
        'permission_id',
        ForeignKey("sys_permission.id"),
        primary_key=True
    )