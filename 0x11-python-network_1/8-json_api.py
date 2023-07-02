#!/usr/bin/python3
"""Send a POST request with parameters."""
import requests
from sys import argv


def main():
    """Entry point of program."""
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(argv) == 1 else argv[1]
    data = {"q": letter}
    response = requests.post(url, data=data)
    try:
        result = response.json()
        if result == {}:
            print("No result")
        else:
            print(f'[{result.get("id")}] {result.get("name")}')
    except ValueError:
        print("Not a valid JSON")
