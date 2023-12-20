#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
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
    data = session.query(State).order_by(State.id)

    for items in data:
        if items.id < 2:
            print(f"{items.id}: {items.name}")
