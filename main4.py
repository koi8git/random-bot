import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🎲 Бот для генерации чисел\n\n"
        "Напишите:\n"
        "• на дабл → 00-99\n"
        "• на трипл → 100-999\n"
        "• на квадрипл → 1000-9999"
    )

# Обработчик личных сообщений (обычный)
@dp.message()
async def private_handler(message: types.Message):
    if not message.text:
        return
    
    text = message.text.lower()
    
    if text == 'на дабл':
        result = random.randint(0, 99)
        await message.answer(f"{result:02d}")
    elif text == 'на трипл':
        await message.answer(str(random.randint(100, 999)))
    elif text == 'на квадрипл':
        await message.answer(str(random.randint(1000, 9999)))

# Обработчик гостевых сообщений
@dp.guest_message()
async def guest_handler(guest_message: types.Message):
    if not guest_message.text:
        return
    
    text = guest_message.text.lower()
    
    if 'на дабл' in text:
        result = random.randint(0, 99)
        await guest_message.answer(f"{result:02d}")
    elif 'на трипл' in text:
        await guest_message.answer(str(random.randint(100, 999)))
    elif 'на квадрипл' in text:
        await guest_message.answer(str(random.randint(1000, 9999)))

async def main():
    print("🤖 Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
