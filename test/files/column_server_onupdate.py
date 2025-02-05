from sqlalchemy import Column
from sqlalchemy.orm import registry
from sqlalchemy.sql import functions as func
from sqlalchemy.types import Integer

reg: registry = registry()


@reg.mapped
class ColumnServerOnUpdateArgument:
    __tablename__ = "onupdate"

    # overload 1: (__name: str, *args, ...)
    overload1: int = Column("name", server_onupdate=func.now(), nullable=False)
    # overload 2: (*args, ...)
    Column(server_onupdate=func.now(), nullable=False)
    # overload 3: (__name: str, __type: _TE, *args, ...)
    overload3 = Column("name", Integer, server_onupdate=func.now(), nullable=False)
    # overload 4: (__type: _TE, *args, ...)
    overload4 = Column(Integer, server_onupdate=func.now(), nullable=False)
