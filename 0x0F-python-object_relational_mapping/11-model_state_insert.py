#!/usr/bin/python3
"""
    Script that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa.
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

    """Add new state and commit to table."""
    n_state = State(name="Louisiana")
    session.add(n_state)
    session.commit()
    print(n_state.id)

    session.close()
