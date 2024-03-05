import strawberry
from pypika import Query as PypikaQuery
from models import engine
from schema import Note
from typing import Any, List
from sqlalchemy import text


def get_notes() -> List[Note]:
    """
    A query function to get all the notes from the database.
    Returns a list of Note objects.
    """
    q = PypikaQuery.from_("m_notes").select("*")
    print(q)
    try:
        with engine.connect() as conn:
            result = conn.execute(text(str(q)))
            # data = dictfetchall(result)
            data = result.mappings().all()

    except Exception as e:
        print(e)
        return "error"
    
    return data


@strawberry.type
class Query:
    notes: List[Note] = strawberry.field(resolver=get_notes)
