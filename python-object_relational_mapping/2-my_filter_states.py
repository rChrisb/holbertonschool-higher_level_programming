#!/usr/bin/python3
"""Filter  by user input"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        password=password,
        database=database
        )
    cursor = connection.cursor()
    cursor.execute(
        "SELECT*from states WHERE BINARY name = '{}'".format(sys.argv[4])
        )

    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    connection.close()
