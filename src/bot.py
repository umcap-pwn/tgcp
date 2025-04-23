#! ../venv/bin/python


import colorlog
from telegram import Bot
from utils import PersistentMessage
from monitor import get_system_status
import logging
import asyncio


handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '[%(log_color)s%(levelname)s%(reset)s]: %(message)s',
    log_colors={
        'DEBUG':    'bold_cyan',
        'INFO':     'bold_blue',
        'WARNING':  'bold_yellow',
        'ERROR':    'bold_red',
        'CRITICAL': 'bold_red,bg_yellow'
    }
))

logging.basicConfig(
    level=logging.INFO,
    handlers=[handler]
)

TOKEN = ""
CHAT_ID = None

async def main():
    try:
        bot = Bot(TOKEN)
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

