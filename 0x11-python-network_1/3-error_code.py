#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8) and an error message if needed
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            answer = response.read().decode('utf-8')
            print(answer)
    except urllib.error.HTTPError as Error:
        print("Error code: {}".format(Error.code))
