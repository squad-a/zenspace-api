import strawberry
from models import Notes, Session, engine, User
from schema import User as UserSchema
import uuid
from datetime import datetime
from utils import generated_avatar_url, is_user_exists
from pypika import Table, Query as PypikaQuery
from sqlalchemy import text
import secrets
from schema import SuccessResponse, ErrorResponse
from typing import Annotated, Union, List

# Todo: Adding Avatar URL


LoginResponse = Annotated[
    Union[SuccessResponse[UserSchema], ErrorResponse], strawberry.union("LoginResponse")
]

RegisterResponse = Annotated[
    Union[SuccessResponse[str], ErrorResponse],
    strawberry.union("RegisterResponse"),
]


@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_user(self, email: str) -> RegisterResponse:
        avatar_url = generated_avatar_url()

        session = Session()
        user_exist = is_user_exists(email)

        if user_exist:
            return ErrorResponse(message="User Already Exists")

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

            return SuccessResponse(
                data="",
                message="User Created Successfully",
            )


    @strawberry.mutation
    def login_user(self, email: str) -> LoginResponse:
        """
        This function is used to authenticate the user.
        :param email: str
        :return: str
        """

        user_exist = is_user_exists(email)
        
        if user_exist:
            session_id = str(secrets.token_hex(16))
            try:
                user = Table("m_user")
                with engine.connect() as conn:
                    q = (
                        PypikaQuery.update(user)
                        .set(user.session_id, session_id)
                        .where(user.email == email)
                    )

                    result = conn.execute(text(str(q)))
                    conn.commit()
                    conn.close()

                with engine.connect() as conn:
                    q = user.select("*").where(user.email == email)
                    result = conn.execute(text(str(q)))
                    user_data = result.mappings().all()
                    print("user_data", user_data)
                    print(
                        "user_data",
                        UserSchema(
                            user_id=user_data[0]["user_id"],
                            email=user_data[0]["email"],
                            avatar=user_data[0]["user_id"],
                            created_at=user_data[0]["created_at"],
                            session_id=session_id,
                            is_active=user_data[0]["is_active"],
                        ),
                    )
                    return SuccessResponse(
                        data=UserSchema(
                            user_id=user_data[0]["user_id"],
                            email=user_data[0]["email"],
                            avatar=user_data[0]["user_id"],
                            created_at=user_data[0]["created_at"],
                            session_id=session_id,
                            is_active=user_data[0]["is_active"],
                        ),
                        message="Login Successful",
                    )

            except Exception as e:
                print(e)
                return ErrorResponse(message="Login Failed")
        else:
            return ErrorResponse(message="User Not Found")

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
