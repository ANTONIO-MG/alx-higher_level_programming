#!/bin/bash
# script takes in a URL, sends a POST request to passed URL, and displays the body of response.
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
