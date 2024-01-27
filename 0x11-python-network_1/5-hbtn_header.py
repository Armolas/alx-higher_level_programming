#!/usr/bin/python3
"""gets the header of a request"""
if __name__ == "__main__":
    import requests
    import sys
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
