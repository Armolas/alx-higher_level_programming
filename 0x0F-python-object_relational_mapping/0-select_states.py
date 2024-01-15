#!/bin/python3
"""This module selects all states from states table"""


if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * from states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
