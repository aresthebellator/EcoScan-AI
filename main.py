from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

input_messages = [
    {
        "role": "user",
        "content": "Ciao come stai"
    }
]

response = client.responses.create(
    model="gpt-4o-mini",
    input = input_messages
)


print(response.output_text)
