from typing import Optional, List

from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from hello_db.models import User, HiBase
from app import db_engine


class UserManager:
    def __init__(self, user_model=User, engine=db_engine, base=HiBase):
        self._user_model = user_model
        self._engine = engine
        self._base = base

    def init_table(self) -> None:
        self._user_model.__table__.create(self._engine)

    def drop_table(self) -> None:
        self._user_model.__table__.drop(self._engine)

    def get_all_users(self) -> List[User]:
        with Session(self._engine) as session:
            users = session.execute(select(self._user_model)).all()

            return users

    def add_user(self, name: str, surname: Optional[str] = None) -> None:
        with Session(self._engine) as session:
            user = self._user_model(name=name, surname=surname)

            session.add(user)
            session.commit()

    def check_user_exists(
            self, name: str, surname: Optional[str] = None
    ) -> bool:

        with Session(self._engine) as session:
            exists_query = (
                select(self._user_model).where(
                    self._user_model.name == name,
                    self._user_model.surname == surname
                ).exists()
            )

            return session.execute(
                select(exists_query)
            ).first()[0]
