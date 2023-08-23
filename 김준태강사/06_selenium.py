import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def get_naver_search(driver: WebDriver, search_test: str) -> str:
    driver.get('https://naver.com')
    time.sleep(3)
    search_input = driver.find_element(By.CSS_SELECTOR, '#query')
    search_input.send_keys(search_test)
    search_button = driver.find_element(By.CSS_SELECTOR, '.btn_search')
    search_button.click()
    return driver.page_source

def get_price_with_soup(soup: BeautifulSoup) -> str:
    return soup.select_one('.spt_con strong').text.strip()



web_driver = webdriver.Chrome(
        service=Service(executable_path=r'C:\tools\Webdriver\chromedriver-win64\chromedriver.exe'))
searched_soup = BeautifulSoup(get_naver_search(web_driver, '에코프로'), 'html.parser')
print(f'price : {get_price_with_soup(searched_soup)}')
web_driver.quit()


