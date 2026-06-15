from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8460466817:AAEFLm0S11ysyR_oR-oCQB8KuFaYlkQGNf0"  # 🔐 حطه هنا
ADMIN_ID = 970041902  # 🔐 حط رقمك الحقيقي

API = f"https://api.telegram.org/bot{TOKEN}"

@app.route("/")
def home():
    return "Bot is running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    if not data or "message" not in data:
        return "ok"

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    # رد للعميل
    requests.post(API + "/sendMessage", json={
        "chat_id": chat_id,
        "text": "✅ تم استلام رسالتك وسيتم الرد قريبًا"
    })

    # إرسال للأدمن
    requests.post(API + "/sendMessage", json={
        "chat_id": ADMIN_ID,
        "text": f"📩 رسالة جديدة:\n{text}"
    })

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
