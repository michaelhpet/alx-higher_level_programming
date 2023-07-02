#!/usr/bin/python3
"""Get 10 most recent commits in repository."""
import requests
import sys


def main():
    """Entry point of program."""
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2],
        sys.argv[1]
    )
    response = requests.get(url)
    commits = response.json()
    try:
        commits = commits[:10]
        for commit in commits:
            print("{} {}".format(
                commit.get("sha"),
                commit.get("commit").get("author").get("name")
            ))
    except Exception:
        pass


if __name__ == "__main__":
    main()
