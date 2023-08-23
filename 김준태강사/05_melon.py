import csv
from bs4 import BeautifulSoup
import requests

def crawl_melon(melon_soup):
    songs = melon_soup.select('.lst50')
    result = [['제목', '가수', '앨범']]
    for s in songs:
        song = s.select_one('.rank01 a').text.strip()
        singer = s.select_one('.rank02 a').text.strip()
        album = s.select_one('.rank03 > a').text.strip()
        result.append([song, singer, album])
    with open('song_top50.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(result)


def crawl_melon2(melon_soup):
    songs = melon_soup.select('.lst50 .rank01 a')
    singers = melon_soup.select('.lst50 .rank02 a')
    albums = melon_soup.select('.lst50 .rank03 > a')
    result = [['제목', '가수', '앨범']]
    for i in range(50):
        song = songs[i].text.strip()
        singer = singers[i].text.strip()
        album = albums[i].text.strip()
        result.append([song, singer, album])
    with open('song_top50_2.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(result)

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
melon = requests.get('https://www.melon.com/chart/index.htm', headers=headers)
melon_soup = BeautifulSoup(melon.text, 'html.parser')

crawl_melon(melon_soup)
crawl_melon2(melon_soup)
