#!/usr/bin/python3
"""fetches a url using requests"""
if __name__ == "__main__":
    import requests
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"    - type: {type(r.text)}")
    print(f"    - content: {r.text}")
