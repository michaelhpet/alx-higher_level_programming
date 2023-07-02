#!/usr/bin/python3
"""Get 10 most recent commits in repository."""
import requests
from sys import argv


def main():
    """Entry point of program."""
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            print("{} {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")
            ))
    except IndexError:
        pass


if __name__ == "__main__":
    main()
