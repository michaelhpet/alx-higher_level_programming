#!/usr/bin/python3
"""Delete states.

A script to delete all State objects with a name containing the letter `a`
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """Entry point of program."""
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.contains("a"))
    for state in states:
        session.delete(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
