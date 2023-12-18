#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    """
    imports the database and then makes a query
    """
    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    mycursor = connection.cursor()

    mycursor.execute("select * from cities order by id asc")

    for items in mycursor:
        print(items)
