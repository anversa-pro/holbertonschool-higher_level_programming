#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
and displays status information
"""
import requests


if __name__ == "__main__":
    """
    This script fetches a URL with an urllib
    and displays info of the status
    """
    response = requests.get('https://intranet.hbtn.io/status')
    response = response.text

    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(response), response))
