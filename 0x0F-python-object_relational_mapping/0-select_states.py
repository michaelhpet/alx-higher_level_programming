#!/usr/bin/python3
"""Get all states.

A script that lists all states from the database hbtbn_0e_0_usa
- takes 3 arguments: `mysql username`
, `mysql password`, `database name`
- connects to MySQL server running on `localhost` at port `3306`
- results are sorted in ascending order by states.id
"""
import MySQLdb
from sys import argv


def main():
    """Entry point of program."""
    connection = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id;")
    results = cursor.fetchall()
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
