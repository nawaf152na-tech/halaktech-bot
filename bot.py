import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 🔐 التوكن من Render Environment Variables
TOKEN = os.getenv("TOKEN", "")

# 🧑‍💼 رقم حسابك من Render Environment Variables
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# 🚀 رسالة البداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بك في Halak Tech Digital\n"
        "📩 اكتب رسالتك وسيتم الرد عليك من فريق الدعم."
    )

# 📩 تحويل الرسائل للأدمن
async def forward_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    message = f"""
📩 رسالة جديدة من عميل

👤 الاسم: {user.first_name}
🆔 اليوزر: @{user.username if user.username else 'لا يوجد'}
🆔 ID: {user.id}

💬 الرسالة:
{update.message.text}
"""

    # إرسال للأدمن
    await context.bot.send_message(chat_id=ADMIN_ID, text=message)

    # رد للعميل
    await update.message.reply_text(
        "✅ تم استلام رسالتك، سيتم الرد عليك قريبًا من فريق Halak Tech Digital."
    )

# 🚀 تشغيل البوت
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_admin))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
