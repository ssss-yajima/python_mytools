import json
import urllib.request
import os

LINE_ENDPOINT = "https://notify-api.line.me/api/notify"
### LINE ACCESS KEY ###
LINE_KEY=os.environ.get("LineKey")


# Line notification 
def notify(msg):
    method = "POST"
    headers = {"Authorization": "Bearer %s" % LINE_KEY}
    payload = {"message": msg}
    try:
        payload = urllib.parse.urlencode(payload).encode("utf-8")
        req = urllib.request.Request(
            url=LINE_ENDPOINT, data=payload, method=method, headers=headers)
        urllib.request.urlopen(req)
    except Exception as e:
        print ("Exception Error: ", e)
        sys.exit(1)
