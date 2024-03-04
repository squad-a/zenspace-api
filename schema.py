import strawberry
from typing import Generic, List, TypeVar

T = TypeVar("T")


@strawberry.type
class Note:
    note_id: str
    note: str
    created_at: str
    is_active: bool
    user_id: str | None


@strawberry.type
class User:
    user_id: str
    email: str
    avatar: str
    created_at: str
    session_id: str | None
    is_active: bool


@strawberry.type
class SuccessResponse(Generic[T]):
    data: T
    message: str


@strawberry.type
class ErrorResponse:
    message: str

