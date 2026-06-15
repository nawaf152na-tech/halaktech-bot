import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

# 📩 فقط تحويل الرسائل لك
async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text

    msg = f"""📩 رسالة جديدة

👤 الاسم: {user.first_name}
🆔 اليوزر: @{user.username}
🆔 ID: {user.id}

💬 الرسالة:
{text}
"""

    await context.bot.send_message(chat_id=ADMIN_ID, text=msg)

app = ApplicationBuilder().token(TOKEN).build()

# 🚫 بدون /start بدون ترحيب بدون أي شيء
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward))

print("Bot running...")
app.run_polling()
