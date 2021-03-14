from sqlalchemy import Integer, String, Date
from sqlalchemy.sql.schema import Column, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    height = Column(Integer, nullable=False)
    dob = Column(Date, nullable=False)

    team_id = Column(Integer, ForeignKey('teams.id'))
