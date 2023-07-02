#!/usr/bin/python3
"""Send a request and display value of X-Request-Id."""
from urllib.request import Request, urlopen
from sys import argv


def main():
    """Entry point of program."""
    url = argv[1]
    request = Request(url)
    with urlopen(request) as response:
        headers = dict(response.headers)
        print(headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
