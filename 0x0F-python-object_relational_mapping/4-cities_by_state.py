#!/bin/python3
"""This module selects cities and states"""


if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name from cities \
                LEFT JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
