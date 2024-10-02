import telebot
from telebot import types

# Bot tokeni
bot = telebot.TeleBot('7827577986:AAGJ3tYTyU7gsaQ9m2Nxx3F2MVkOkeT9Opw')


# Inline queryni qabul qilish va ishlov berish
@bot.inline_handler(lambda query: 'ko\'paytir' in query.query and any(char.isdigit() for char in query.query))
def inline_query(query):
    try:
        # Query'dan sonni ajratib olish
        query_text = query.query.lower().replace("ko'paytir", "").strip()  # "ko'paytir" so'zini olib tashlash
        number = int(query_text)  # Kiritilgan sonni olish
        result = number * 12  # Sonni 12ga ko'paytirish

        # Inline natija yaratish
        r = types.InlineQueryResultArticle(
            id='1',
            title=f"Natija: {result}",
            description=f"{number} * 12 = {result}",
            input_message_content=types.InputTextMessageContent(
                message_text=f"Natija: {number} * 12 = {result}"
            )
        )

        # Inline queryga javob yuborish
        bot.answer_inline_query(query.id, [r])

    except Exception as e:
        print(e)


# Botni ishga tushirish
bot.polling()
