#!/usr/bin/python3
"""Get all states"""

import MySQLdb
import sys


username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
connection = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    database='hbtn_0e_0_usa'
)

cursor = connection.cursor()
cursor.execute("SELECT * from states ORDER BY id ASC")
results = cursor.fetchall()
for row in results:
    print(row)

cursor.close()
connection.close()
