#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""

import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], stname=sys.argv[4],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
            WHERE CONVERT(`name` USING Latin1) \
            COLLATE Latin1_General_Cs = f'{sys.argv[4]}';")
    rows = cur.fetchall()
    for row in rows:
        print(row)