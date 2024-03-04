import random
from pypika import Table
from models import engine
from sqlalchemy import text


def generated_avatar_url() -> str:
    """
    This function is used to generate a random avatar url.
    :return: str
    """

    i = 0
    url = "https://source.boringavatars.com/pixel/120/Maria%20Mitchell?colors="
    while i < 5:
        color = random.randint(0, 2**24)
        hex_color = hex(color)
        if i == 0:
            url += hex_color[2:]
        else:
            url += "," + hex_color[2:]
        i += 1

    return url


def is_user_exists(email: str) -> bool:
    """
    This function is used to check if the user exists in the database.
    :param email: str
    :return: bool
    """

    user = Table("m_user")
    q = user.select("*").where(user.email == email)
    with engine.connect() as conn:
        result = conn.execute(text(str(q)))
        user_data = result.mappings().all()

        if user_data:
            return True
        else:
            return False
