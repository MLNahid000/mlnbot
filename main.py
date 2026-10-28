import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# /start কমান্ডে রিপ্লাই দিবে
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalamu Alaikum! 🤖\nAmi MLN Bot, Ami Online Achi ✅")

# বট চালু করার ফাংশন
def main():
    TOKEN = os.environ.get("BOT_TOKEN")
    if not TOKEN:
        print("BOT_TOKEN set kora hoy nai!")
        return
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("MLN Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
