from sqlalchemy import (
    Column,
    Integer,
    String,
)

from .base import Base


class Donut(Base):
    __tablename__ = 'donuts'

    id = Column(Integer, primary_key=True)
    donut = Column(String, unique=True)
    description = Column(String)

    def __repr__(self):
        return (
            f"<Donut(id={self.id}, "
            f"donut='{self.donut}', "
            f"description='{self.description}')>"
        )
