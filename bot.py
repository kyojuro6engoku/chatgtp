import os
import telebot
from transformers import pipeline
# Initialize the ChatGPT model
model = pipeline("text-generation", model="EleutherAI/finetuned-gpt-neo-1.3B")
# Initialize the Telegram bot
bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))
# Define the function to handle incoming messages
def handle_message(message):
    # Get the message text
    text = message.text
    # Generate a response using the ChatGPT model
    response = model(text, max_length=1024)
    # Send the response to the user
    bot.send_message(message.chat.id, response["generated_text"])
# Start the Telegram bot
bot.polling()
