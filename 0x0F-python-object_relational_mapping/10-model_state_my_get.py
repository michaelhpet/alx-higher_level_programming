#!/usr/bin/python3
"""Get a state.

A script to print the `State` object with the `name` passed as argument
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def main():
    """Entry point of program."""
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == argv[4]).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)


if __name__ == "__main__":
    main()
