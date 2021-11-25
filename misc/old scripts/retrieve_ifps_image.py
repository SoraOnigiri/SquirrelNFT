import requests
import json

SQUIRREL_LIBRARY = "QmZVzEmMV8VjMnLVUGYV6ygFnAGk2Efw1JQVwmyieZgrNL"

ipfs_url = "http://127.0.0.1:5001"
endpoint = f"/api/v0/file/ls?arg={SQUIRREL_LIBRARY}"
response = requests.post(ipfs_url + endpoint)
# print(response.content)
r = response.content.decode()
rs = json.loads(r)
tokenuri_list = rs["Objects"][SQUIRREL_LIBRARY]["Links"]

with open("./assets/imageuri.json", "w") as file:
    json.dump(tokenuri_list, file)
