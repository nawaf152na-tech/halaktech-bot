import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أرسل رسالتك وسيتم تحويلها للدعم.")

async def forward_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    message = f"""
📩 رسالة جديدة
👤 {user.first_name}
🆔 {user.id}

💬 {update.message.text}
"""

    await context.bot.send_message(chat_id=ADMIN_ID, text=message)
    await update.message.reply_text("تم إرسال رسالتك.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_admin))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
