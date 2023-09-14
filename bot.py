import os
import telegram
import openai

# Set your Telegram Bot API token and OpenAI API key as environment variables
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Initialize the Telegram Bot
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

# Initialize the OpenAI API
openai.api_key = OPENAI_API_KEY

# Define a function to handle incoming Telegram messages
def handle_message(update, context):
    user_id = update.message.chat_id
    user_message = update.message.text
    
    # Send the user's message to ChatGPT
    response = send_to_chatgpt(user_message)
    
    # Send the ChatGPT response back to the user
    context.bot.send_message(chat_id=user_id, text=response)

# Define a function to interact with ChatGPT
def send_to_chatgpt(user_message):
    # Customize the prompt to ChatGPT as needed
    prompt = f"User: {user_message}\nAI:"
    
    # Send the user's message to ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose the appropriate ChatGPT engine
        prompt=prompt,
        max_tokens=50  # Adjust based on your desired response length
    )
    
    return response.choices[0].text.strip()

# Create a Telegram updater and dispatcher
from telegram.ext import Updater, MessageHandler, Filters

updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add a message handler to the dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Start polling for updates
updater.start_polling()
updater.idle()