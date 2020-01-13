#2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

import requests
import json

url = 'http://ws.audioscrobbler.com/2.0/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117'
}
params = {
    'api_key': 'a1b516681b06dc9b0c2ca4404294b7ad',
    'method': 'chart.gettopartists',   # picked this method between others from API documentation
    'format': 'json'
}

response = requests.get(url, headers=headers, params=params)

with open('response2.json', 'w') as outfile:  # writing data to json file
    json.dump(response.json(), outfile)

def jprint(obj):  # function for readable representation
    data = json.dumps(obj, sort_keys=True, indent=4)
    print(data)

jprint(response.json())
