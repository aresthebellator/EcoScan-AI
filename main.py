import os
import base64
import json
import requests
import smtplib
from email.mime.text import MIMEText
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes, ConversationHandler, CommandHandler

# ------------------- CONFIG -------------------
TELEGRAM_TOKEN = "8375572558:AAHYjfaNU0ldW1T_QnYMLnwZbsZIUtNgZ1w"
LLAVA_MODEL = "llava"
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Dizionario comuni -> email
COMUNI_EMAIL = {
    "Catania": "comune@catania.it",
    "Roma": "comune@roma.it",
    "Milano": "comune@comune.milano.it",
    "Napoli": "comune@comune.napoli.it",
    "Torino": "comune@comune.torino.it",
    "Palermo": "comune@comune.palermo.it",
    "Bologna": "comune@comune.bologna.it",
    "Firenze": "comune@comune.firenze.it",
    "Genova": "comune@comune.genova.it",
    "Venezia": "comune@comune.venezia.it",
    
}

ASK_COMUNE = 1  

# ------------------- FUNZIONE ANALISI -------------------
def analyze_text_or_image(text_prompt, image_path=None):
    """
    Analizza testo o testo+immagine tramite LLaVA e restituisce la risposta
    """
    payload = {"model": LLAVA_MODEL, "prompt": text_prompt}
    if image_path:
        with open(image_path, "rb") as f:
            img_b64 = base64.b64encode(f.read()).decode()
        payload["images"] = [img_b64]

    response = requests.post("http://localhost:11434/api/generate", json=payload, stream=True)
    full_text = ""
    for line in response.iter_lines():
        if not line:
            continue
        try:
            data = json.loads(line.decode("utf-8"))
        except json.JSONDecodeError:
            continue
        if "response" in data:
            full_text += data["response"]
        if data.get("done", False):
            break
    return full_text

# ------------------- FUNZIONE EMAIL -------------------
def send_email_alert(subject, body, to_email):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "tuoemail@gmail.com"
    msg['To'] = to_email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login("tuoemail@gmail.com", EMAIL_PASSWORD)
        server.send_message(msg)

# ------------------- HANDLER TELEGRAM -------------------
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Riceve foto dall'utente, verifica preliminarmente se ci sono rifiuti significativi
    """
    message = update.message
    photo_file = await message.photo[-1].get_file()  # Prende la foto ad alta risoluzione
    photo_path = f"temp_{photo_file.file_id}.jpg"
    await photo_file.download_to_drive(photo_path)  # Scarica localmente

    context.user_data["photo_path"] = photo_path
    context.user_data["caption"] = message.caption if message.caption else ""

    await message.reply_text("🔍 Verifico se ci sono accumuli di rifiuti nella foto...")

    # Analisi preliminare: capire se c'è rifiuti e gravità
    prelim_prompt = (
        "Sei un assistente che valuta accumuli di rifiuti. Rispondi solo nel formato:\n"
        "Presenza: sì/no\nGravità: bassa/media/alta\nQuantità: minima/moderata/grande\n"
        "Solo per decidere se inviare segnalazione. Non chiedere comune.\n"
        "Input aggiuntivo: " + context.user_data["caption"]
    )

    try:
        result = analyze_text_or_image(prelim_prompt, photo_path)
        result_lower = result.lower()

        # Se gravità almeno media o quantità moderata/grande, chiedi il comune
        if ("sì" in result_lower or "si" in result_lower) and ("media" in result_lower or "alta" in result_lower or "moderata" in result_lower or "grande" in result_lower):
            await message.reply_text("📍 Ci sono accumuli rilevanti! In quale comune è stata scattata la foto?")
            return ASK_COMUNE
        else:
            await message.reply_text("✅ Nessun accumulo significativo rilevato nella foto.")
            return ConversationHandler.END
    except Exception as e:
        await message.reply_text("❌ Errore durante l'analisi preliminare.")
        print(e)
        return ConversationHandler.END

async def ask_comune(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Dopo che l'utente ha risposto con il comune
    """
    comune = update.message.text.strip()
    photo_path = context.user_data.get("photo_path")
    user_text = context.user_data.get("caption", "")

    if comune not in COMUNI_EMAIL:
        await update.message.reply_text("❌ Comune non trovato. Inserisci un comune valido.")
        return ASK_COMUNE

    to_email = COMUNI_EMAIL[comune]

    prompt = (
        "Sei un assistente che analizza accumuli di rifiuti in città. Rispondi nel formato:\n"
        "Tipo_rifiuti: ...\nQuantità: ...\nGravità: bassa/media/alta\nSuggerimenti: ...\n"
        "Informazioni aggiuntive: " + user_text
    )

    await update.message.reply_text("🔍 Analizzo la scena completa, attendi...")

    try:
        result = analyze_text_or_image(prompt, photo_path)
        await update.message.reply_text(f"♻️ Analisi dei rifiuti:\n{result}")

        if "gravità: alta" in result.lower():
            send_email_alert(
                subject=f"Segnalazione rifiuti urgente - {comune}",
                body=f"Il bot EcoScan-AI ha rilevato un grande accumulo di rifiuti.\n\nDettagli:\n{result}",
                to_email=to_email
            )
            await update.message.reply_text(f"⚠️ Gravità alta rilevata! Email inviata al comune di {comune}.")
    except Exception as e:
        await update.message.reply_text("❌ Errore durante l'analisi completa.")
        print(e)
    finally:
        if os.path.exists(photo_path):
            os.remove(photo_path)

    return ConversationHandler.END

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Gestisce i messaggi di solo testo
    """
    user_text = update.message.text
    prompt = (
        "Sei un assistente che analizza accumuli di rifiuti in città. "
        "Rispondi nel formato:\nTipo_rifiuti: ...\nQuantità: ...\nGravità: bassa/media/alta\nSuggerimenti: ...\n"
        "Input utente: " + user_text
    )

    await update.message.reply_text("📖 Analizzo il testo...")

    try:
        result = analyze_text_or_image(prompt)
        await update.message.reply_text(f"📝 Analisi:\n{result}")
    except Exception as e:
        await update.message.reply_text("❌ Errore durante l'analisi del testo.")
        print(e)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Ciao! Inviami una foto o un testo per analizzare accumuli di rifiuti.")

# ------------------- AVVIO DEL BOT -------------------
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.PHOTO, handle_photo)],
        states={ASK_COMUNE: [MessageHandler(filters.TEXT & (~filters.COMMAND), ask_comune)]},
        fallbacks=[]
    )

    app.add_handler(conv_handler)
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_text))
    app.add_handler(CommandHandler("start", start))

    print("Bot EcoScan-AI avviato!")
    app.run_polling()

if __name__ == "__main__":
    main()