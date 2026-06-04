from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = 8785236581:AAHiuKwec_mqOoZb0gNH-pdDP08D6oztLzY

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я CNDRAW бот 🤖\nОтправь мне PDF-чертёж, и я его обработаю."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()