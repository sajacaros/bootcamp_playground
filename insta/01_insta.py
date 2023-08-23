## selenium, webdriver 설치 확인
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def load_insta():
    driver = webdriver.Chrome(service=Service(executable_path=r'C:\tools\Webdriver\chromedriver-win64\chromedriver.exe'))
    driver.implicitly_wait(3)
    url = "https://www.instagram.com"
    driver.get(url=url)
    return driver

def login(driver, id, pw):
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(id)
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(pw)
    # driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER)
def search_tag(driver, hashtag, scroll_times=2):
    url = f"https://www.instagram.com/explore/tags/{hashtag}"
    driver.get(url=url)
    time.sleep(10)

    for _ in range(scroll_times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

driver = load_insta()
id = os.getenv("INSTA_ID")
pw = os.getenv("INSTA_PW")
login(driver, id, pw)
time.sleep(5)

hashtag = "강아지"
search_tag(driver, hashtag, 3)
