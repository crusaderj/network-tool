import urllib.request
import re

print("we will try to open this url, in order to get IP Address")

url = "http://checkip.dyndns.org"

with urllib.request.urlopen(url) as response:
    html = response.read().decode("utf-8")
theIP = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", html)

print("your IP Address is: {}".format(theIP))
