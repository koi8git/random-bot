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

# ПРАВИЛЬНЫЙ обработчик гостевых сообщений через перехват Update
@dp.update()
async def handle_guest_mode(update: types.Update):
    # Проверяем, является ли входящий апдейт гостевым сообщением
    if not update.guest_message:
        return  # Если это обычное сообщение или другой апдейт, выходим
        
    guest_msg = update.guest_message
    if not guest_msg.text:
        return
    
    text = guest_msg.text.lower()
    text_reply = ""
    
    # Логика проверки команд
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
    
    # Отправляем ответ через answer_guest_query
    await bot.answer_guest_query(
        guest_query_id=guest_msg.guest_query_id,
        text=text_reply
    )

async def main():
    print("🤖 Бот запущен!")
    print("📨 Режимы: личные сообщения + гостевой режим")
    # Явно указываем Telegram, что мы хотим получать гостевые сообщения,
    # иначе по умолчанию он их не присылает в polling!
    await dp.start_polling(bot, allowed_updates=["message", "guest_message"])

if __name__ == "__main__":
    asyncio.run(main())
