#!/usr/bin/python3
"""
script that deletes State names containing a from the hbtn_0e_6_usa db
"""

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sqlalchemy
from sys import argv

h = 'localhost'
sq = 'mysql+mysqldb'

if __name__ == '__main__':
    e = create_engine(f'{sq}://{argv[1]}:{argv[2]}@{h}:3306/{argv[3]}')

    # create a session with the sessionmaker
    Session = sessionmaker(bind=e)

    # configure the session with the engine
    Session.configure(bind=e)

    # create the instance of the session
    # that you will use to communicate with the database
    session = Session()

    # create a python object and query the database and hold the details
    data = session.query(State).filter(State.name.contains('a'))

    # loop and delete all queried data
    for items in data:
        session.delete(items)
    session.commit()
