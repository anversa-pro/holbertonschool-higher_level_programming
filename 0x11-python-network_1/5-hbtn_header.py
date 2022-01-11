#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
"""
import requests
import sys


if __name__ == "__main__":
    """
    This script fetches a URL with an urllib
    and displays info of the status
    """
    URL = sys.argv[1]
    response = requests.get(URL)
    print(response.headers.get("X-Request-Id"))
