import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld", data={"channel": "cohhcarnage"})
print(response.json()["data"])

