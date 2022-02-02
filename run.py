from scraper import Scraper
from alerter import MessageSender
elements_to_click: list[str] = ['menu-button-54', 'menu-list-54-menuitem-56', 'menu-button-42',
                                'menu-list-42-menuitem-46']
element_to_wait: str = 'css-427d58'
element_to_query: str = 'css-427d58'

if __name__ == "__main__":
    message_sender: MessageSender = MessageSender()
    scraper: Scraper = Scraper(message_sender)
    scraper.run_scraper(elements_to_click, element_to_wait, element_to_query)
