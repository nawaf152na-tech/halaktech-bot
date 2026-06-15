from flask import Flask, request
import requests
import os

app = Flask(__name__)

# 🔐 القيم من Render (بدون تعديل الكود)
TOKEN = os.getenv("TOKEN", "")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

API = f"https://api.telegram.org/bot{TOKEN}"

@app.route("/")
def home():
    return "Bot is running"

# ✅ Webhook ثابت (بدون مشاكل)
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    if not data or "message" not in data:
        return "ok"

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    # 🤖 رد تلقائي للعميل
    requests.post(API + "/sendMessage", json={
        "chat_id": chat_id,
        "text": "✅ تم استلام رسالتك، وسيتم الرد عليك قريبًا من فريق Halak Tech Digital"
    })

    # 📩 إرسال لك أنت
    requests.post(API + "/sendMessage", json={
        "chat_id": ADMIN_ID,
        "text": f"📩 رسالة جديدة:\n\n{text}"
    })

    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
