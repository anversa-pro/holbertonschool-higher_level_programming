#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    """
    Displays the body of the response
    """
    user = sys.argv[1]
    userpw = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth={user, userpw})
    print(r.json().get('id'))
