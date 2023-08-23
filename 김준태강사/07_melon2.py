import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def crawl_melon(melon_soup):
    songs = melon_soup.select('.lst50')
    result = []
    for s in songs:
        song = s.select_one('.rank01 a').text.strip()
        singer = s.select_one('.rank02 > a').text.strip()
        album = s.select_one('.rank03 > a').text.strip()
        result.append([song, singer, album])
    return result


web_driver = webdriver.Chrome(
    service=Service(executable_path=r'C:\tools\Webdriver\chromedriver-win64\chromedriver.exe'))
web_driver.get('https://www.melon.com/chart/month/index.htm')
time.sleep(3)
month_arrow = web_driver.find_element(By.CSS_SELECTOR, '.m4')
month_arrow.click()
time.sleep(3)
arrow_button = web_driver.find_element(By.CSS_SELECTOR, '.arrow_d')
arrow_button.click()
month_buttons = web_driver.find_elements(By.CSS_SELECTOR, '.month_calendar a')
for month_button in month_buttons:
    month_button.click()
    time.sleep(3)
    month_html = web_driver.page_source
    month_soup = BeautifulSoup(month_html, 'html.parser')
    print(crawl_melon(month_soup))

web_driver.quit()
