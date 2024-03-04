import strawberry
from models import Notes, Session, engine, User
from schema import User as UserSchema
import uuid
from datetime import datetime
from utils import generated_avatar_url, is_user_exists
from pypika import Table, Query as PypikaQuery
from sqlalchemy import text
import secrets
from schema import LoginSuccess, LoginError
from typing import Annotated, Union

# Todo: Adding Avatar URL


LoginResponse = Annotated[
    Union[LoginSuccess, LoginError], strawberry.union("LoginResponse")
]


@strawberry.type
class Mutation:
    @strawberry.mutation
    def signup(self, email: str) -> str:
        avatar_url = generated_avatar_url()

        session = Session()
        user_exist = is_user_exists(email)

        if user_exist:
            return "User Already Exists"

        else:
            user = User(
                user_id=str(uuid.uuid4()),
                email=email,
                avatar=avatar_url,
                created_at=datetime.utcnow(),
                is_active=True,
            )
            session.add(user)
            session.commit()
            session.close()

            return "User Registered Successfully"




    # * API is Underconstruction

    @strawberry.mutation
    # def login(self, email: str) -> LoginResponse:
    #     """
    #     This function is used to authenticate the user.
    #     :param email: str
    #     :return: str
    #     """

    #     user_exist = is_user_exists(email)
    #     if user_exist:
    #         session_id = str(secrets.token_hex(16))
    #         try:
    #             user = Table("m_user")
    #             with engine.connect() as conn:
    #                 q = (
    #                     PypikaQuery.update(user)
    #                     .set(user.session_id, session_id)
    #                     .where(user.email == email)
    #                 )
    #                 print(q)
    #                 result = conn.execute(text(str(q)))
    #                 conn.commit()
    #                 conn.close()

    #             with engine.connect() as conn:
    #                 q = user.select("*").where(user.email == email)
    #                 result = conn.execute(text(str(q)))
    #                 user_data = result.mappings().all()

    #             return LoginSuccess(data=User(**user_data))

    #         except Exception as e:
    #             return LoginError(message="Login Failed")
    #     else:
    #         return LoginError(message="User Not Found")

    @strawberry.mutation
    def add_notes(self, note: str) -> str:
        """
        This function is used to add notes to the database.
        :param note: str
        :return: str
        """

        session = Session()
        note = Notes(
            note_id=str(uuid.uuid4()),
            note=note,
            created_at=datetime.utcnow(),
            is_active=True,
            user_id=None,
        )
        session.add(note)
        session.commit()
        session.close()

        return "Data Saved Successfully"
