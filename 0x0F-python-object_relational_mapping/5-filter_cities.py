#!/usr/bin/python3
"""This module selects cities of a particular state"""


if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name from states JOIN cities ON \
                cities.state_id = states.id WHERE cities.state_id = \
                (SELECT id from states WHERE states.name = %s) \
                ORDER BY cities.id ASC", (sys.argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        for col in row:
            if col != rows[-1][0]:
                print(col, end=', ')
            else:
                print(col)
