#!/usr/bin/python3
"""
python file that contains the class definition of a State and an instance Base
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    class with the properties for a state
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return "<State(name:'%s', id= '%s')>" % (name, id)
