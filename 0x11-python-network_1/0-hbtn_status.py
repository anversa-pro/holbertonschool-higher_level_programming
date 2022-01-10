#!/usr/bin/python3
""" Script to fetch https://intranet.hbtn.io/status
    and display the status
"""
import urllib.request


if __name__ == "__main__":
    """
    This script fetches a domain using urllib
    and displays the body of the response
    """
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as request:
        statusInfo = request.read()
        print("Body response:")
        print("\t- type:", type(statusInfo))
        print("\t- content:", statusInfo)
        print("\t- utf8 content:", str(statusInfo)[2:-1])
