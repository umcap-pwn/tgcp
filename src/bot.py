from telegram import Bot
from utils import PersistentMessage
import monitor
import logging


#Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,  
    format='[%(levelname)s]: %(message)s',
    handlers=[logging.StreamHandler()]  
)

TOKEN = ""
CHAT_ID =   

bot = Bot(TOKEN)
panel = PersistentMessage(bot, CHAT_ID, "🖥️ Контрольная панель запущена")


panel.update_text("CPU: 15%\nRAM: 34%")


time.sleep(5)
panel.clear()