from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import base64
import requests

def vision_ollama(image_path):
    with open(image_path, "rb") as f:
        img = base64.b64encode(f.read()).decode()

    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "moondream2",
            "prompt": "Descrivi l'immagine:",
            "images": [img]
        }
    )
    return r.json()["response"]

print(vision_ollama("foto.jpg"))