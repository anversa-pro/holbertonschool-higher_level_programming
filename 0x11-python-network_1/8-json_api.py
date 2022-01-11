#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
and verify Json file formant and content.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        value = ""
    else:
        value = sys.argv[1]

    resp = requests.post('http://0.0.0.0:5000/search_user', data={'q': value})
    try:
        answer = resp.json()
        if len(answer) == 0:
            print("No result")
        else:
            print("[{}] {}".format(answer["id"], answer["name"]))
    except Exception as error:
        print("Not a valid JSON")
