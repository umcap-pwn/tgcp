#! ../venv/bin/python

import colorlog
from telegram import Bot
from utils import PersistentMessage
from monitor import get_system_status
from dotenv import load_dotenv
import os
import logging
import asyncio

logging.getLogger('httpx').setLevel(logging.WARNING)

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '[%(log_color)s%(levelname)s%(reset)s]: %(message)s',
    log_colors={
        'DEBUG':    'bold_cyan',
        'INFO':     'bold_blue',
        'WARNING':  'bold_yellow',
        'ERROR':    'bold_red',
        'CRITICAL': 'bold_red,bg_white'
    }
))




logging.basicConfig(
    level=logging.INFO,
    handlers=[handler]
)

BOT_CHAT_ID = None
BOT_TOKEN = None


async def main():
    try:
        BOT_TOKEN = os.getenv("BOT_TOKEN")
        BOT_CHAT_ID = os.getenv("BOT_CHAT_ID")
        if BOT_TOKEN and BOT_CHAT_ID:
            bot = Bot(TOKEN)
        else:
            logging.info("Для работы бота необходимо предоставить ID чата и токен бота.")
            logging.info("Введите токен бота:")
            _ = input().strip() 
            BOT_TOKEN =  _ if ":" in _ and len(_) > 30 else None
            
            logging.info("Введите ID чата:")
            BOT_CHAT_ID = int(input())
            if BOT_CHAT_ID and BOT_TOKEN:
                set_key(env_path, "BOT_CHAT_ID",str(BOT_CHAT_ID))
                set_key(env_path, "BOT_TOKEN", str(BOT_TOKEN))
            return
        panel = PersistentMessage(bot, CHAT_ID)
        await panel.initialize("Контрольная панель запущена")

        while True:
            try:
                status = get_system_status()
                await panel.update_text(status)
                await asyncio.sleep(5)
            except Exception as e:
                logging.error(f"Error in main loop: {e}")
                await asyncio.sleep(5)

    except Exception as e:
        logging.error(f"Fatal error: {e}")
    finally:
        if 'panel' in locals():
            await panel.clear()

if __name__ == "__main__":
    asyncio.run(main())

