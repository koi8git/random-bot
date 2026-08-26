import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = os.environ.get('TELEGRAM_TOKEN')
if not TOKEN:
    raise ValueError("TELEGRAM_TOKEN не найден!")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🎲 Бот для генерации чисел\n\n"
        "Напишите:\n"
        "• на дабл → 00-99\n"
        "• на трипл → 100-999\n"
        "• на квадрипл → 1000-9999"
    )

@dp.message()
async def scan(message: types.Message):
    if message.chat.type != "private":
        return
    if not message.text:
        return
    
    text = message.text.lower()
    
    if text == 'на дабл':
        await message.answer(f"{random.randint(0, 99):02d}")
    elif text == 'на трипл':
        await message.answer(str(random.randint(100, 999)))
    elif text == 'на квадрипл':
        await message.answer(str(random.randint(1000, 9999)))

async def main():
    print("🤖 Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
