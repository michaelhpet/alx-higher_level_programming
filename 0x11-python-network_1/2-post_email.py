#!/usr/bin/python3
"""Send a post request to mail server."""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv


def main():
    """Entry point of program."""
    url = argv[1]
    body = {"email": argv[2]}
    body = urlencode(body).encode("ascii")
    request = Request(url)
    with urlopen(request) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    main()
