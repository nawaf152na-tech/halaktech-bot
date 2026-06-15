import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك 👋 أرسل رسالتك وسيتم الرد عليك")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    msg = f"""رسالة جديدة:
الاسم: {user.first_name}
اليوزر: @{user.username}
ID: {user.id}

الرسالة:
{update.message.text}"""

    await context.bot.send_message(chat_id=ADMIN_ID, text=msg)

    await update.message.reply_text("تم استلام رسالتك ✅")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

print("Bot running...")
app.run_polling()
