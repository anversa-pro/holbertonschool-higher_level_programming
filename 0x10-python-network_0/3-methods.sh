#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -siX OPTIONS "$1" | grep Allow: | cut -d " " -f 1 --complement
