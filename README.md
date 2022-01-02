# New Token Alerter

Python application that scrapes information about new tokens from DEX Screener periodically and sends subscribers a 
notification of newly listed tokens via Telegram.

## Set up

- Create telegram bot
- Store access token for bot in environment variable `TELEGRAM_BOT_TOKEN` 

## Current Configuration

Currently, the program is specifically coded to navigate to the page showing Aurora tokens listed in the last hour with
a minimum liquidity of $50K every 30 seconds to check if any new tokens have been listed.