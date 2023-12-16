#!/usr/bin/python3
#  script that lists all states from the database hbtn_0e_0_usa

import sys
import mysql.connector

if __name__ == '__main__':
    # imports the database and then makes a query
    connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2]
    )
    mycursor = connection.cursor()
    mycursor.execute("use hbtn_0e_0_usa")
    mycursor.execute("select * from states")

    for items in mycursor:
        print(items)
