#!/bin/bash
# Script that sends a JSON POST request to a URL passed as
# the first argument, and displays the body of the response.
curl -sd @"$2" -X POST "$1" -H "Content-Type: application/json"
