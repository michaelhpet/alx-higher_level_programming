#!/usr/bin/python3
"""Fetch https://alx-intranet.hbtn.io/status."""
from urllib.request import Request, urlopen


def main():
    """Entry point of program."""
    url = "https://alx-intranet.hbtn.io/status"
    request = Request(url)
    with urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == "__main__":
    main()
