#!/bin/bash
# Takes in a URL, sends the given URL request, print size of response body
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2