#!/usr/bin/python3
"""Cities in state.

Class definition of a City
"""
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sys import argv
from model_state import Base


class City(Base):
    """Define a City object.

    Attributes:
        id (int): unique identifier of city
        name (str): name of city
        state_id (int): unique id of city's state
    """

    __tablename__ = "cities"

    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)


if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')

    Base.metadata.create_all(engine)
