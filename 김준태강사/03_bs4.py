
from bs4 import BeautifulSoup
import requests

html = '''
<html> 
    <head> 
    </head> 
    <body> 
        <h1> 장바구니
            <p id='clothes' class='name' title='라운드티'> 라운드티
                <span class = 'number'> 25 </span> 
                <span class = 'price'> 29000 </span> 
                <span class = 'menu'> 의류</span> 
                <a href = 'http://www.naver.com'> 바로가기 </a> 
            </p> 
            <p id='watch' class='name' title='시계'> 시계
                <span class = 'number'> 28 </span>
                <span class = 'price'> 32000 </span> 
                <span class = 'menu'> 액세서리 </span> 
                <a href = 'http://www.facebook.com'> 바로가기 </a> 
            </p> 
        </h1> 
    </body> 
</html>
'''

soup = BeautifulSoup(html, 'html.parser')

result = soup.select('a')
print('tag', '-'*10)
print(result)

result = soup.select('.number')
print('class', '-'*20)
print(result)

result = soup.select('p#watch')
print('id', '-'*20)
print(result)

result = soup.select('body > h1')
print('직계 child', '-'*20)
print(result)

result = soup.select('body h1') 
print('모든 child', '-'*20)
print(result)

print('값 뽑기', '-'*20)
result = soup.select('#watch .price')
print(result[0].text.strip())
