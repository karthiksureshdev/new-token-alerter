import telegram as tm
import json
import heapq
import time
from constants import TELEGRAM_BOT_TOKEN
from constants import DEX_SCREENER_URL
from bs4 import Tag, ResultSet


class MessageSender:
    def __init__(self):
        self.bot: tm.Bot = tm.Bot(token=TELEGRAM_BOT_TOKEN)
        self.tokens_seen: set[str] = set()
        self.token_ages: list[tuple[int, str]] = []
        self.send_to_all_members("Token alerter bot is alive :)")

    def __del__(self):
        self.send_to_all_members("Token alerter bot has died :(")

    def get_members(self):
        update: tm.Update
        members: set[str] = set()
        for update in self.bot.get_updates():
            members.add(update.effective_chat.id)
        return members

    def send_to_all_members(self, message: str):
        print(f"Message to send: \n{message}")
        print(f"Message sent to: ")
        member: str
        for member in self.get_members():
            print(f"{member}")
            self.bot.send_message(member, message)

    def send_update(self, tags: ResultSet) -> None:
        message: str = self._tags_to_message(tags)
        print(f"Message to send: \n{message}")
        if not message:
            return None
        self.send_to_all_members(message)

    def clear_old_tokens(self):
        while (time.time() - self.token_ages[0][0]) > 3600:
            token: tuple[int, str] = heapq.heappop(self.token_ages)
            self.tokens_seen.remove(token[1])
            print(f"Cleared from seen tokens: {token[1]}")

    def _tags_to_message(self, tags: ResultSet) -> str:
        message: str = ""
        tag: Tag
        for tag in tags:

            if tag.attrs.get('href') in self.tokens_seen:
                continue

            message += json.dumps({
                'Name': tag.contents[0].contents[2].contents[0].contents[0] +
                        tag.contents[0].contents[2].contents[1].contents[0] +
                        tag.contents[0].contents[2].contents[2].contents[0],
                'Ref': DEX_SCREENER_URL + tag.attrs.get('href'),
                'Age': tag.contents[2].contents[0],
                'Volume ($)': tag.contents[5].contents[0],
                'Liquidity ($)': tag.contents[10].contents[0]
            }, indent=4)
            message += "\n\n"
            self.tokens_seen.add(tag.attrs.get('href'))
            heapq.heappush(self.token_ages, (time.time(), tag.attrs.get('href')))
        return message
