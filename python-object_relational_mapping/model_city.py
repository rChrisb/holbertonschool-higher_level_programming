#!/usr/bin/python3
"""First state model"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
import MySQLdb

Base = declarative_base()


class City(Base):
    """links to the MySQL table states"""
    __tablename__ = "cities"

    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user="root",
        password="root"
        )
