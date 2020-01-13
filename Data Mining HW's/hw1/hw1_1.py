#1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.

import requests
import json

url = 'https://api.github.com/users/fabpot/repos'
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'Accept': 'application/vnd.github.v3+json'
}  # added Accept like in recommendation API documents

response = requests.get(url, headers = headers)

with open('response1.json', 'w') as outfile:   # writing data to json file
    json.dump(response.json(), outfile)

def jprint(obj):  # function for readable representation
    data = json.dumps(obj, sort_keys=True, indent=4)
    print(data)

jprint(response.json())
