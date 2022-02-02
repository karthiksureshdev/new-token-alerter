import re
import time
from logger import LoggingHandler
from bs4 import BeautifulSoup, ResultSet
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from alerter import MessageSender
from constants import DEX_SCREENER_URL, NEW_PAIRS


class Scraper(LoggingHandler):
    TIMEOUT: int = 60
    LOOP_INTERVAL: int = 60

    def __init__(self, message_sender: MessageSender):
        super().__init__()
        self.chrome_options: Options = Options()
        # self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--no-sandbox")
        self.browser: Chrome = self._refresh_browser()
        self.message_sender: MessageSender = message_sender

    def _refresh_browser(self) -> Chrome:
        self.log.info(f"Refreshing Browser")
        self.browser = Chrome(executable_path=ChromeDriverManager().install(), options=self.chrome_options)
        self.browser.get(DEX_SCREENER_URL + NEW_PAIRS)
        return self.browser

    def run_scraper(self, elements_to_click: list[str], element_to_wait: str, element_to_lookup: str):
        element_id: str
        element: WebElement
        while True:
            try:
                for element_id in elements_to_click:
                    self.log.info(f"Waiting for element: {element_id}")
                    element = WebDriverWait(self.browser, Scraper.TIMEOUT) \
                        .until(EC.element_to_be_clickable((By.ID, element_id)))
                    element.click()
                    self.log.info(f"Clicked element: {element_id}")

                self.log.info(f"Waiting for element: {element_to_wait}")
                WebDriverWait(self.browser, Scraper.TIMEOUT) \
                    .until(EC.element_to_be_clickable((By.CLASS_NAME, element_to_wait)))

                self.log.info(f"Finding elements: {element_to_lookup}")
                soup: BeautifulSoup = BeautifulSoup(self.browser.page_source, 'html.parser')
                tags: ResultSet = soup.find_all(class_=re.compile(element_to_lookup))
                self.message_sender.send_update(tags)

                self.log.info(f"Sleeping for {Scraper.LOOP_INTERVAL} seconds.")
                time.sleep(Scraper.LOOP_INTERVAL)
            except Exception as e:
                self.log.exception("Bad message run!")
                self._refresh_browser()


