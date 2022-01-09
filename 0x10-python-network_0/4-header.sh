#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response 
curl -sXH GET "$1"/apply?X-School-User-Id=98
