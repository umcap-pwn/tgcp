from telegram import Bot
from telegram.error import TelegramError
import logging


class PersistentMessage(): 
    def __init__(self, bot: Bot, chat_id: int, initial_message: str = "Initializing bot..."):
        
        self.bot = bot
        self.chat_id = chat_id
        self.message_id = None
        self._create_initial_message(initial_message)
    
        
    def _create_initial_message(self, message: str):
        try:
            self.msg = self.bot.send_message(
                chat_id = self.chat_id,
                text = message,
                parse_mode = "HTML"
            )
        except TelegramError as e:
            logging.error(f"Can't send initial message: {e}")
            
    def update_text(self, new_text: str):
        if not self.msg.message_id:
            logging.error("Message not found")
            return
            
            
        try:
            self.bot.edit_message_text(
                chat_id = self.chat_id,
                message_id = msg.message_id,
                text = new_text,
                parse_mode = "HTML"
            )
        except TelegramError as e:
            logging.error("Can't update message: {e}")
        
        
            
            

print("utils module loaded!")


