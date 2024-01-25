#!/bin/bash
# Sends a DELETE request to the URL as the first argument and displays the body response.
curl -s "$1" -X DELETE