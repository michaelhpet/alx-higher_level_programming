#!/usr/bin/python3
"""Cities by state.

A script to list all cities
"""
import MySQLdb
from sys import argv


def main():
    """Entry point of program."""
    connection = MySQLdb.connect(
                                host="localhost",
                                port=3306,
                                user=argv[1],
                                passwd=argv[2],
                                db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT c.id, c.name, s.name FROM cities c \
                    LEFT JOIN states s \
                    ON s.id = c.state_id \
                    ORDER BY c.id;")
    results = cursor.fetchall()
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
