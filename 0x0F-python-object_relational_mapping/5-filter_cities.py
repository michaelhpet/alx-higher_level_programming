#!/usr/bin/python3
"""All cities by state.

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
    arg = extract_arg(argv[4])
    cursor.execute(f"SELECT c.name FROM cities c \
                    WHERE c.state_id IN ( \
                        SELECT s.id FROM states s \
                        WHERE s.name = '{arg}' \
                    ) \
                    ORDER BY c.id;")
    results = cursor.fetchall()
    print(", ".join(map(lambda x: x[0], results)))


def extract_arg(query: str):
    """Create safe arg for db query."""
    return query.split(";")[0].strip()


if __name__ == "__main__":
    main()
