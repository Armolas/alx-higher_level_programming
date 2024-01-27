#!/usr/bin/python3
"""handles error from requests"""
if __name__ == "__main__":
    import requests
    import sys
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
