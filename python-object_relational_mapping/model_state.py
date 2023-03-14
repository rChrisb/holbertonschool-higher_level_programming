#!/usr/bin/python3
"""First state model"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import MySQLdb

Base = declarative_base()


class State(Base):
    """links to the MySQL table states"""
    __tablename__ = "states"

    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user="root",
        password="root"
        )
