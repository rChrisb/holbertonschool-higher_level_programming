#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

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
    cursor.execute("SELECT * from states ORDER BY id ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    connection.close()
