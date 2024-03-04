from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy.dialects.sqlite import TEXT

import datetime

Base = declarative_base()

engine = create_engine(
    "sqlite:///database.db", echo=True, connect_args={"check_same_thread": False}
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class User(Base):
    __tablename__ = "m_user"

    user_id = Column(String(200), primary_key=True)
    email = Column(String(200), nullable=False)
    avatar = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=True)
    session_id = Column(String(200), nullable=True)


class Notes(Base):
    __tablename__ = "m_notes"

    note_id = Column(String(200), primary_key=True, nullable=False)
    note = Column(TEXT)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=True)
    user_id = Column(String(200))


class MapNotesTags(Base):
    __tablename__ = "map_notes_tags"

    map_id = Column(String(200), primary_key=True, nullable=False)
    note_id = Column(String(200))
    tag_id = Column(Integer)


class Tags(Base):
    __tablename__ = "m_tags"

    tag_id = Column(Integer, primary_key=True, nullable=False)
    tag = Column(String(50))


Base.metadata.create_all(engine)
