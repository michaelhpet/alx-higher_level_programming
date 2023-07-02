#!/usr/bin/python3
"""Fetch https://alx-intranet.hbtn.io/status."""
import requests


def main():
    """Entry point of program."""
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")


if __name__ == "__main__":
    main()
