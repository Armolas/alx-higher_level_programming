#!/usr/bin/env bash
#displays all HTTP methods the server will accept.
curl -sIX OPTIONS $1 | grep -i 'Allow' | cut -d ' ' -f 2-