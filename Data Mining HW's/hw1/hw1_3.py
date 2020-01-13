import requests
import json

url = 'https://5ka.ru/api/v2/categories/'
headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117'
    }

response_category = requests.get(url, headers=headers)  # receiving list of categories

class CategoryObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

result_category = [CategoryObject(**itm) for itm in response_category.json()]  # making list usable with builder

def GetData(payload):  # scruping function for goods
    url_offers = 'https://5ka.ru/api/v2/special_offers/'
    payload['records_per_page'] = '50'
    data = requests.get(url_offers, headers=headers, params=payload)
    return data

parsing_results = []
i = 0

for i in range(len(result_category)):  # composing data with while loop help
    response_goods = GetData({
        'categories': result_category[i].parent_group_code
    })
    parsing_results.append([result_category[i].parent_group_code, result_category[i].parent_group_name, response_goods.json()['results']])
    i += 1
    print(f'parsed {i} out of {len(result_category)} pages')


with open('response3.json', 'w') as outfile:  # writing data in json file
    json.dump(parsing_results, outfile)


print(1)