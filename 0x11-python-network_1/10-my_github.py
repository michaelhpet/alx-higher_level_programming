#!/usr/bin/python3
"""Display GitHub ID."""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def main():
    """Entry point of program."""
    url = f"https://api.github.com/user"
    auth = HTTPBasicAuth(argv[1], argv[2])
    response = requests.get(url, auth=auth)
    user = response.json()
    print(user.get("id"))


if __name__ == "__main__":
    main()
