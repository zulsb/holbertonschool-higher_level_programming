#!/usr/bin/python3
"""
    Script that lists all State objects from the database hbtn_0e_6_usa.
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
    session = Session(engine)

    """Search python instances in database."""
    for state in session.query(State).order_by(State.id):
        print("{:d}: {:s}".format(state.id, state.name))
    session.close()
