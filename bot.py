import os
from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = os.getenv("TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"

@app.route("/", methods=["GET"])
def home():
    return "Bot is running"

@app.route(f"/webhook/{TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # رد للعميل
        requests.post(f"{TELEGRAM_API}/sendMessage", json={
            "chat_id": chat_id,
            "text": "✅ تم استلام رسالتك وسيتم الرد عليك قريبًا من فريق Halak Tech Digital"
        })

        # إرسال لك
        requests.post(f"{TELEGRAM_API}/sendMessage", json={
            "chat_id": ADMIN_ID,
            "text": f"📩 رسالة جديدة:\n\n{text}"
        })

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
