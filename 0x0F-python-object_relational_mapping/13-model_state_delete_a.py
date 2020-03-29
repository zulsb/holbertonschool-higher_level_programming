#!/usr/bin/python3
"""
    Script that deletes all State objects with a name
    containing the letter a from the database hbtn_0e_6_usa.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":

    """Make engine for database."""
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    """Find all states to be deleted with letter a."""
    states = session.query(State).filter(State.name.like('%a%')).all()
    for d in states:
        session.delete(d)
    session.commit()
    session.close()
