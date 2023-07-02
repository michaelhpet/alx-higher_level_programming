#!/usr/bin/python3
"""Send a request and display X-Request-Id header."""
import requests
from sys import argv


def main():
    """Entry point of program."""
    url = argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
