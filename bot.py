from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 မင်္ဂလာပါ။ ကျွန်တော်က **Eren AI Bot** ပါ။\n"
        "မေးချင်တာမေးလို့ရပါတယ်။ အချိန်မရွေး ကူညီဖြေကြားပေးပါ့မယ်။ 💪"
    )

async def gemini_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    try:
        response = model.generate_content(user_msg)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text(f"❌ အမှားအယွင်းဖြစ်သွားပါတယ်။\nError: {str(e)}")

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, gemini_reply))
    print("🤖 Eren AI Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
