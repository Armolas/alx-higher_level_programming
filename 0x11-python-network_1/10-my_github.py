#!/usr/bin/python3
"""Displays Github id"""
if __name__ == "__main__":
    import requests
    import sys
    url = f"https://api.github.com/{sys.argv[1]}"
    token = f"Bearer {sys.argv[2]}"
    header = {'Authorization': token,
              'Accept': 'application/vnd.github+json',
              "X-GitHub-Api-Version": "2022-11-28"}
    r = requests.get(url, headers=header)
    json = r.json()
    print(json.get('id'))
