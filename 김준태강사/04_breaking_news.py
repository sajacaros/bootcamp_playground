import csv
from bs4 import BeautifulSoup as bs, ResultSet, Tag
import requests


def crawl_naver(category, date, page):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    url = f'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1={category}&date={date}&page={page}'
    print(url)

    breaking_news = requests.get(url, headers=headers)

    soup = bs(breaking_news.text, 'html.parser')
    headline_cards = soup.select('ul.type06_headline > li')

    result = [['제목','본문일부','신문사','작성시각']]
    for card in headline_cards:
        headline_title = card.select('dt > a')[-1].text.strip()
        headline_contents = card.select('span')[0].text.strip()
        headline_writer = card.select('span')[1].text.strip()

        result.append([headline_title, headline_contents, headline_writer, date])
    
    with open('news_headline.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(result)

news_no = 101
crawl_naver(news_no, '20230803', 1)