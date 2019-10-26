import requests
import json
from pprint import pprint

tag = 'pyhton'

data_url ='https://api.stackexchange.com/2.2/answers/'

params = {
    'order':    'desc',
    'sort':     'activity',
    'tagged':   tag,
    'site':     'stackoverflow',
    'filter':   '!9Z(-wzu0T'
    }

data = requests.get(data_url, params=params)
data_d = data.json()

print(data.url)
pprint(data_d)

# запись данных data_d в формат файл 'data_d_json.json' формата json
with open('data_d_json.json', 'w') as d_file:
    json.dump(data_d, d_file)
    d_file_str = json.dumps(data_d)

# print(type(d_file_str))

# считывание данных из файла 'data_d_json.json' в data_d_j типа dict
with open('data_d_json.json', 'r') as d_file_read:
    data_d_j  = json.load(d_file_read)

# pprint(data_d_j['items'][1]['creation_date'])
#
# print(type(data_d_j))

