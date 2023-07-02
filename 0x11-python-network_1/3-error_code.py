#!/usr/bin/python3
"""Send a request and display response."""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv


def main():
    """Entry point of program."""
    url = argv[1]
    request = Request(url)
    try:
        with urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as ex:
        print(f"Error code: {ex.code}")


if __name__ == "__main__":
    main()
