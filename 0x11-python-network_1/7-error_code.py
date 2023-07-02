#!/usr/bin/python3
"""Send a request and display response."""
import requests
from sys import argv


def main():
    """Entry point of program."""
    url = argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
