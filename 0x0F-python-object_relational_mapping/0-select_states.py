#!/usr/bin/python3
#  script that lists all states from the database hbtn_0e_0_usa

import sys
import Mysqldb

from SQLalchemy import connect, 

if __name__ == '__main__':
    # imports the database and then makes a quere on the same database that has been imported
    connection MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
    