import asyncio
import logging
from datetime import datetime, timedelta
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = "8244806173:AAHZiM-yO9CAl45-Cmvix0bEGoP80TnJ54"
CHANNEL_ID = -1708258221

# Запуск бота
logging.basicConfig(level=logging.INFO)
bot = Bot(token=8244806173:AAHZiM-y09CAl45-Cmvix0bOEGoP80TnJ54, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    try:
        expire_time = datetime.now() + timedelta(seconds=60)
        invite_link = await bot.create_chat_invite_link(
            chat_id=CHANNEL_ID,
            expire_date=expire_time,
            member_limit=1
        )
      
        kb = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text="ЗАБРАТЬ", url=invite_link.invite_link)
        ]])
      
        msg = await message.answer(
            text="Твоя ссылка готова. У тебя ровно **60 секунд**, чтобы забрать его и зайти в канал. Время пошло!!!",
            reply_markup=kb
        )
      
        await asyncio.sleep(60)

        await bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
        await message.answer("Время вышло. Твоя персональная ссылка уничтожена. Бесплатный вход сгорел.")

    except Exception as e:
        await message.answer("Ошибка создания ссылки. Проверь, добавлен ли бот в админы канала.")
        logging.error(f"Ошибка: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
  
