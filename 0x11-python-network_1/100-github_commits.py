#!/usr/bin/python3
"""Get 10 most recent commits in repository."""
import requests
from sys import argv


def main():
    """Entry point of program."""
    url = f"https://api.github.com/repos/{argv[1]}/{argv[2]}/commits"
    response = requests.get(url)
    commits = response.json()
    commits = commits[:10]
    for commit in commits:
        print("{} {}".format(
            commit.get("sha"),
            commit.get("commit").get("author").get("name")
        ))


if __name__ == "__main__":
    main()
