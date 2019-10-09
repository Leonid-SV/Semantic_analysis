import requests

data = requests.get('https://api.stackexchange.com/2.2/answers?page=1&order=desc&max=1569628800&sort=activity&site=stackoverflow')

print(data.content)

