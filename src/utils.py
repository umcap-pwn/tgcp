import asyncio
from telegram import Bot
from telegram.error import TelegramError
import logging


class PersistentMessage():
    def __init__(self, bot: Bot, chat_id: int):
        self.bot = bot
        self.chat_id = chat_id
        self.message_id = None
        self.msg = None

    

    
    async def initialize(self, initial_message: str = "Инициализация бота..."):
        await self._create_initial_message(initial_message)
        return self

    

    
    async def _create_initial_message(self, message: str):
        try:
            self.msg = await self.bot.send_message(
                chat_id=self.chat_id,
                text=message,
                parse_mode="HTML"
            )
            self.text = message
            self.message_id = self.msg.message_id
        except TelegramError as e:
            print(e)
            logging.error(f"Не удается отправить начальное сообщение: {e}")

    

    
    async def update_text(self, new_text: str):
        if new_text == self.text:
            return
        try:
            if self.msg:
                await self.bot.edit_message_text(
                    chat_id=self.chat_id,
                    message_id=self.msg.message_id,
                    text=new_text,
                    parse_mode="HTML"
                )
                self.text = new_text
        except TelegramError as e:
            if "Message to edit not found" in str(e):
                await self._create_initial_message("...") 
            else:
                logging.warning(f"Не удается обновить сообщение: {e}.")

    

    
    async def clear(self):
        try:
            if self.msg:
                await self.bot.delete_message(
                    chat_id=self.chat_id,
                    message_id=self.msg.message_id
                )
                self.text = None
                self.msg = None
        except TelegramError as e:
            logging.error(f"Не удается удалить сообщение: {e}")
                
    






print("utils module loaded!")


