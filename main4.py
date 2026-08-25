import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.enums import MessageEntityType
from aiogram.filters import Command
from aiogram import F

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🎲 Бот для генерации чисел\n\n"
        "Напишите:\n"
        "• на дабл → 0-99\n"
        "• на трипл → 100-999\n"
        "• на квадрипл → 1000-9999"
    )

# Обработчик личных сообщений (только НЕ гостевые)
@dp.message(F.text & ~F.guest_message)
async def private_handler(message: types.Message):
    text = message.text.lower()
    
    if text == 'на дабл':
        await message.answer(str(random.randint(0, 99)))
    elif text == 'на трипл':
        await message.answer(str(random.randint(100, 999)))
    elif text == 'на квадрипл':
        await message.answer(str(random.randint(1000, 9999)))

# Обработчик гостевых сообщений (упоминание в чате)
@dp.message(F.text & F.guest_message)
async def guest_handler(message: types.Message):
    # Проверяем, упомянули ли бота
    has_mention = False
    if message.entities:
        for entity in message.entities:
            if entity.type == MessageEntityType.MENTION:
                mention_text = message.text[entity.offset:entity.offset + entity.length]
                if mention_text.lower() == '@numbergod_bot':
                    has_mention = True
                    break
    
    if not has_mention:
        return
    
    text = message.text.lower()
    
    if 'на дабл' in text:
        await message.reply(str(random.randint(0, 99)))
    elif 'на трипл' in text:
        await message.reply(str(random.randint(100, 999)))
    elif 'на квадрипл' in text:
        await message.reply(str(random.randint(1000, 9999)))

async def main():
    print("🤖 Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
