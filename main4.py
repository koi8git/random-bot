import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.guest_message()
async def handle_guest_mode(message: types.Message):
    if not message.text:
        return
        
    text = message.text.lower()
    
    # Генерация логики числа
    if 'на дабл' in text or 'дабл' in text:
        text_reply = f"🎲 Ваше число: {random.randint(0, 99):02d}"
    elif 'на трипл' in text or 'трипл' in text:
        text_reply = f"🎲 Ваше число: {random.randint(100, 999)}"
    elif 'на квадрипл' in text or 'квадрипл' in text:
        text_reply = f"🎲 Ваше число: {random.randint(1000, 9999)}"
    else:
        return # Если ключевых слов нет, бот просто молчит

    # Чтобы сообщение улетало текстом в чат при обычном гостевом вызове:
    result_card = types.InlineQueryResultArticle(
        id=str(random.randint(1, 100000)),
        title="Результат генерации", 
        input_message_content=types.InputMessageContent(
            message_text=text_reply # Этот текст бот отправит прямо в чат
        )
    )

    await message.answer_guest_query(results=[result_card])

async def main():
    print("🤖 Бот готов к гостевому текстовому режиму!")
    await dp.start_polling(bot, allowed_updates=["message", "guest_message"])

if __name__ == "__main__":
    asyncio.run(main())
