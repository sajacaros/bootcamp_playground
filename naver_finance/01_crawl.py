import requests

url = "https://finance.naver.com/item/main.naver"
params = {'code': '005930'}
res = requests.get(url, params)
print(res.text)