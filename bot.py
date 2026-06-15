import os
from flask import Flask, request
import requests

app = Flask(__name__)

# 🔐 القيم من Render
TOKEN = os.getenv("TOKEN", "")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"

@app.route("/", methods=["GET"])
def home():
    return "Bot is running"

# 🚀 Webhook ثابت (بدون توكن في الرابط)
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    if not data:
        return "no data"

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # رد للعميل
        requests.post(f"{TELEGRAM_API}/sendMessage", json={
            "chat_id": chat_id,
            "text": "✅ تم استلام رسالتك وسيتم الرد عليك قريبًا من فريق Halak Tech Digital"
        })

        # إرسال للأدمن
        requests.post(f"{TELEGRAM_API}/sendMessage", json={
            "chat_id": ADMIN_ID,
            "text": f"📩 رسالة جديدة:\n\n{text}"
        })

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
