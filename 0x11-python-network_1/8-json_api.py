#!/usr/bin/python3
"""takes in a letter and sends a POST request to\
    http://0.0.0.0:5000/search_user with the letter as a parameter."""
if __name__ == "__main__":
    import requests
    import sys
    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': letter})
    json = r.json()
    if json:
        id = json.get('id')
        name = json.get('name')
        if id and name:
            print(f"[{id}] {name}")
        else:
            print("Not a valid JSON")
    else:
        print("No result")
