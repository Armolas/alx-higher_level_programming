#!/bin/bash
#sends a post request with a json file
curl -H "Content-Type: application/json" -d @$2 -sX POST $1
