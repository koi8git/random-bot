import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик обычных сообщений
@dp.message()
async def scan(message: types.Message):
    text = message.text.lower()
    
    if text == 'на дабл':
        await message.answer(random.randint(0, 99))
    elif text == 'на трипл':
        await message.answer(random.randint(100, 999))
    elif text == 'на квадрипл':
        await message.answer(random.randint(1000, 9999))

# Обработчик гостевых запросов (Guest Mode)
@dp.guest_message()
async def handle_guest(message: types.Message, guest_query_id: str):
    text = message.text.lower()
    
    if text == 'на дабл':
        await bot.answer_guest_query(guest_query_id, result=str(random.randint(0, 99)))
    elif text == 'на трипл':
        await bot.answer_guest_query(guest_query_id, result=str(random.randint(100, 999)))
    elif text == 'на квадрипл':
        await bot.answer_guest_query(guest_query_id, result=str(random.randint(1000, 9999)))
    else:
        await bot.answer_guest_query(guest_query_id, result="Отправьте: 'На дабл', 'На трипл' или 'На квадрипл'")

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
