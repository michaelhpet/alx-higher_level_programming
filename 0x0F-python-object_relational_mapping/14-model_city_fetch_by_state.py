#!/usr/bin/python3
"""Cities in state.

A script to print all `City` objects.
"""
from model_city import City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def main():
    """Entry point of program."""
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Session = sessionmaker(engine)
    session = Session()

    cities_and_states = session.query(City, State).join(State).all()
    for city, state in cities_and_states:
        print(f"{state.name:s}: ({city.id:d}) {city.name:s}")
    session.close()


if __name__ == "__main__":
    main()
