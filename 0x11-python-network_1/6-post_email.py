#!/usr/bin/python3
"""Send a post request to mail server."""
import requests
from sys import argv


def main():
    """Entry point of program."""
    url = argv[1]
    data = {"email": argv[2]}
    response = requests.post(url, data=data)
    print(response.text)


if __name__ == "__main__":
    main()
