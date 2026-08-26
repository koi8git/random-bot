import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent

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
        "Или упомяните меня в любом чате: @numbergod_bot на дабл"
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
async def handle_guest_mode(guest_message: types.Message):
    if not guest_message.text:
        return
    
    text = guest_message.text.lower()
    
    # Проверяем наличие команд
    if 'на дабл' in text or 'дабл' in text:
        result = random.randint(0, 99)
        formatted_result = f"{result:02d}"
        text_reply = f"🎲 {formatted_result}"
    elif 'на трипл' in text or 'трипл' in text:
        result = random.randint(100, 999)
        text_reply = f"🎲 {result}"
    elif 'на квадрипл' in text or 'квадрипл' in text:
        result = random.randint(1000, 9999)
        text_reply = f"🎲 {result}"
    else:
        text_reply = "❌ Отправьте: 'на дабл', 'на трипл' или 'на квадрипл'"
    
    # Создаем объект результата для гостевого ответа
    result_article = InlineQueryResultArticle(
        id=str(random.randint(1, 1000000)),
        title="Результат",
        input_message_content=InputTextMessageContent(
            message_text=text_reply
        )
    )
    
    # Отправляем ответ через answer_guest_query
    await bot.answer_guest_query(
        guest_query_id=guest_message.guest_query_id,
        result=result_article
    )

async def main():
    print("🤖 Бот запущен!")
    print("📨 Режимы: личные сообщения + гостевой режим")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
