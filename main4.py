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
        "• на квадрипл → 1000-9999\n\n"
        "Или используйте инлайн-режим: @numbergod_bot на дабл"
    )

# Обработчик текстовых сообщений (личные сообщения)
@dp.message()
async def scan(message: types.Message):
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

# ХЕНДЛЕР ДЛЯ ГОСТЕВОГО РЕЖИМА (Inline Query)
@dp.inline_query()
async def handle_guest_mode(inline_query: types.InlineQuery):
    text = inline_query.query.lower().strip()
    
    # Значения по умолчанию
    title = "Выберите режим"
    description = "Введите: на дабл, на трипл или на квадрипл"
    message_text = "Используйте подсказки: напишите 'на дабл', 'на трипл' или 'на квадрипл'"
    
    if text == 'на дабл':
        title = "Генерация Дабла"
        result = random.randint(0, 99)
        message_text = f"Ваше число: {result:02d}"
        description = "Сгенерировать число от 00 до 99"
    elif text == 'на трипл':
        title = "Генерация Трипла"
        result = random.randint(100, 999)
        message_text = f"Ваше число: {result}"
        description = "Сгенерировать число от 100 до 999"
    elif text == 'на квадрипл':
        title = "Генерация Квадрипла"
        result = random.randint(1000, 9999)
        message_text = f"Ваше число: {result}"
        description = "Сгенерировать число от 1000 до 9999"

    # Формируем карточку ответа
    result_card = types.InlineQueryResultArticle(
        id=str(random.randint(1, 100000)),
        title=title,
        description=description,
        input_message_content=types.InputTextMessageContent(
            message_text=message_text
        )
    )
    
    # Отправляем результат пользователю (кеш отключаем)
    await inline_query.answer(results=[result_card], cache_time=1)

async def main():
    print("🤖 Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
