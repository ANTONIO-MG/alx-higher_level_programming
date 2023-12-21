#!/usr/bin/python3
"""
script that lists all Cities  objects from the database hbtn_0e_14_usa
"""

from sqlalchemy.orm import sessionmaker
from model_city import City
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
    data = session.query(City, State).join(State)

    for x, y in data.all():
        print(f"{y.name}: ({x.id}) {x.name}")

    session.commit()
