#!/usr/bin/python3

"""Filter  by user input"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        password=password,
        database=database
        )
    cursor = connection.cursor()
    cursor.execute(
        "SELECT cities.name \
        from cities join states on cities.state_id = states.id\
            WHERE BINARY states.name = %s ORDER BY cities.id", (state_name,)
        )

    results = cursor.fetchall()
    if results:
        for row in range(len(results)):
            if row == len(results) - 1:
                for (city) in results[row]:
                    print(city)
            else:
                for (city) in results[row]:
                    print(city, end=", ")
    else:
        print()

    cursor.close()
    connection.close()
