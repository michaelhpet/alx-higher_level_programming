#!/usr/bin/python3
"""Filter states by user input.

A script to list all states where `name` matches the argument
- takes 3 arguments: `mysql username`, `state name searched`
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
    arg = extract_arg(argv[4])
    cursor.execute(f"SELECT * FROM states WHERE name = '{arg}';")
    results = cursor.fetchall()
    for result in results:
        print(result)


def extract_arg(query: str):
    """Create safe arg for db query."""
    return query.split(";")[0]


if __name__ == "__main__":
    main()
