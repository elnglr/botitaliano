from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import json
import random


def load_data():
    with open('italian_data.json', 'r', encoding='utf-8') as file:
        return json.load(file)
def select_random(data):
    phrase = random.choice(data["phrases"])
    word = random.choice(data["words"])
    return phrase, word

async def respond(update: Update, context):
    data = load_data()
    phrase, word = select_random(data)
    message = f"📚 Daily Italian:\n\n🔹 **Phrase:** {phrase}\n🔹 **Word:** {word}"
    await update.message.reply_text(message, parse_mode="Markdown")

def main():

    BOT_TOKEN = "7932054894:AAGg5MOguOhWxOTfBJolhYg9IlH-0G9jIjg"
    application = Application.builder().token(BOT_TOKEN).build()
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, respond)
    application.add_handler(message_handler)
    application.run_polling()

if __name__ == "__main__":
    main()
