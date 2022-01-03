import re
import time
from bs4 import BeautifulSoup, ResultSet
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.chrome.options import Options
from alerter import MessageSender
from constants import DEX_SCREENER_URL, NEW_PAIRS

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
timeout = 60  # seconds
messageSender: MessageSender = MessageSender()

while True:
    try:
        browser.get(DEX_SCREENER_URL + NEW_PAIRS)

        myElem: WebElement = WebDriverWait(browser, timeout)\
            .until(EC.element_to_be_clickable((By.ID, 'menu-button-47')))
        myElem.click()
        myElem = WebDriverWait(browser, timeout) \
            .until(EC.element_to_be_clickable((By.ID, 'menu-list-47-menuitem-49')))
        myElem.click()
        myElem = WebDriverWait(browser, timeout) \
            .until(EC.element_to_be_clickable((By.ID, 'menu-button-37')))
        myElem.click()
        myElem = WebDriverWait(browser, timeout) \
            .until(EC.element_to_be_clickable((By.ID, 'menu-list-37-menuitem-41')))
        myElem.click()
        myElem = WebDriverWait(browser, timeout) \
            .until(EC.element_to_be_clickable((By.ID, 'menu-button-6')))
        myElem.click()
        myElem = WebDriverWait(browser, timeout) \
            .until(EC.element_to_be_clickable((By.ID, 'menu-list-6-menuitem-15')))
        myElem.click()
        myElem: WebElement = WebDriverWait(browser, timeout) \
            .until(EC.presence_of_element_located((By.CLASS_NAME, 'css-4es7dx')))

        soup: BeautifulSoup = BeautifulSoup(browser.page_source, 'html.parser')
        tags: ResultSet = soup.find_all(class_=re.compile("css-427d58"))

        messageSender.send_update(tags)
        messageSender.clear_old_tokens()

        for i in range(30, 0, -1):
            print(f"Sleeping for {str(i)} seconds.", end="\r")
            time.sleep(1)
        print("\n")
    except Exception as e:
        print(e)
        print("Bad message run!")
        del browser
        browser = webdriver.Chrome(options=chrome_options)


