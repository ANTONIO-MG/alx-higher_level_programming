#!/usr/bin/python3
"""
python file that contains the class definition of a city and an instance Base
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from model_state import State, Base


class City(Base):
    """
    class with the properties for a city
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True,  nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
