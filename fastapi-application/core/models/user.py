from sqlalchemy import Column, Integer, String, UniqueConstraint

from .base import Base  # Assuming base.py contains the Base class


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    foo = Column(Integer)
    bar = Column(Integer)

    __table_args__ = (
        UniqueConstraint("foo", "bar"),
    )
