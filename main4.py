import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я бот для генерации случайных чисел.\n\n"
                         "Отправьте мне:\n"
                         "• На дабл → число от 0 до 99\n"
                         "• На трипл → число от 100 до 999\n"
                         "• На квадрипл → число от 1000 до 9999\n\n"
                         "Также вы можете упомянуть меня в любом чате: @numbergod_bot На дабл")

# Обработчик обычных текстовых сообщений (личные сообщения боту)
@dp.message(F.text & ~F.guest_message)
async def scan(message: types.Message):
    text = message.text.lower()
    
    if text == 'на дабл':
        await message.answer(str(random.randint(0, 99)))
    elif text == 'на трипл':
        await message.answer(str(random.randint(100, 999)))
    elif text == 'на квадрипл':
        await message.answer(str(random.randint(1000, 9999)))
    else:
        await message.answer("Я не понимаю эту команду.\n\n"
                            "Отправьте:\n"
                            "• На дабл\n"
                            "• На трипл\n"
                            "• На квадрипл")

# Обработчик гостевых сообщений (упоминание бота в любом чате)
@dp.message(F.guest_message)
async def handle_guest_message(message: types.Message):
    # Получаем текст сообщения
    text = message.text.lower()
    
    # Получаем ID гостевого запроса
    query_id = message.guest_query_id
    
    if not query_id:
        return
    
    # Определяем результат
    if 'на дабл' in text:
        result_text = str(random.randint(0, 99))
    elif 'на трипл' in text:
        result_text = str(random.randint(100, 999))
    elif 'на квадрипл' in text:
        result_text = str(random.randint(1000, 9999))
    else:
        result_text = "Отправьте: 'На дабл', 'На трипл' или 'На квадрипл'"
    
    # Отправляем ответ через answer_guest_query
    await bot.answer_guest_query(
        guest_query_id=query_id,
        result=InlineQueryResultArticle(
            id=str(random.randint(1, 1000000)),
            title="Результат",
            input_message_content=InputTextMessageContent(
                message_text=result_text
            )
        )
    )

async def main():
    print("🤖 Бот запущен и готов к работе!")
    print(f"👤 Имя бота: @numbergod_bot")
    print("📨 Режим: Обычные сообщения + Гостевой режим")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
