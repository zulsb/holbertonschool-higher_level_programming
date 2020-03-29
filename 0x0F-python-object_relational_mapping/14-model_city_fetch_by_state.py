#!/usr/bin/python3
"""
    Script print all City objects from the database hbtn_0e_14_usa.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City


if __name__ == "__main__":

    """Make engine for database."""
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    """Search multiple tables in database and print information."""
    for s in session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id):
        print("{:s}: ({:d}) {:s}".format(s[0], s[1], s[2]))

    session.close()
