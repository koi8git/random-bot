import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик обычных сообщений
@dp.message(F.text)
async def scan(message: types.Message):
    text = message.text.lower()
    
    if text == 'на дабл':
        await message.answer(str(random.randint(0, 99)))
    elif text == 'на трипл':
        await message.answer(str(random.randint(100, 999)))
    elif text == 'на квадрипл':
        await message.answer(str(random.randint(1000, 9999)))

# Обработчик гостевых сообщений (Guest Mode)
@dp.message(F.guest_message)
async def handle_guest_message(message: types.Message):
    text = message.text.lower()
    query_id = message.guest_query_id
    
    if not query_id:
        return
    
    # Определяем ответ
    if text == 'на дабл':
        result_text = str(random.randint(0, 99))
    elif text == 'на трипл':
        result_text = str(random.randint(100, 999))
    elif text == 'на квадрипл':
        result_text = str(random.randint(1000, 9999))
    else:
        result_text = "Отправьте: 'На дабл', 'На трипл' или 'На квадрипл'"
    
    # Отправляем ответ через answer_guest_query
    await bot.answer_guest_query(
        guest_query_id=query_id,
        text=result_text
    )

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
