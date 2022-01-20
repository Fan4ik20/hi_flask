from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

HiBase = declarative_base()


class User(HiBase):
    __tablename__ = 'HiFlaskUser'

    id = Column(Integer, primary_key=True)

    name = Column(String(30), nullable=False)
    surname = Column(String(50))

    def __repr__(self):
        return f'User - {self.name} {self.surname}'
