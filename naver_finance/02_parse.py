import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.naver"
params = {'code': '005930'}
res = requests.get(url, params)
bs_obj = BeautifulSoup(res.text, 'html.parser')
div_today = bs_obj.find("div", {"class": "today"})
em = div_today.find('em')
price = em.find('span').text
print(price)
