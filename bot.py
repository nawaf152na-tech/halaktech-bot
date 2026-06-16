import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

# نخزن آخر مستخدم
last_user = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("اكتب رسالتك وسيتم إرسالها للدعم.")

async def forward_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    last_user["id"] = user.id

    text = f"""
📩 رسالة جديدة
👤 {user.first_name}
🆔 {user.id}

💬 {update.message.text}
"""

    await context.bot.send_message(chat_id=ADMIN_ID, text=text)

    await update.message.reply_text("تم إرسال رسالتك")

# رد الأدمن
async def reply_to_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    if "id" not in last_user:
        await update.message.reply_text("لا يوجد مستخدم للرد عليه")
        return

    await context.bot.send_message(
        chat_id=last_user["id"],
        text=f"📩 رد الدعم:\n\n{update.message.text}"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_admin))
    app.add_handler(MessageHandler(filters.TEXT & filters.User(ADMIN_ID), reply_to_user))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
