from flask import Flask, request
import requests

app = Flask(__name__)

# 🔴 حط بياناتك هنا مباشرة (للتجربة فقط)
TOKEN = "PUT_YOUR_TOKEN_HERE"
ADMIN_ID = 123456789

API = f"https://api.telegram.org/bot{TOKEN}"

@app.route("/")
def home():
    return "Bot is running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # رد للعميل
        requests.post(API + "/sendMessage", json={
            "chat_id": chat_id,
            "text": "تم استلام رسالتك 👍"
        })

        # رسالة لك
        requests.post(API + "/sendMessage", json={
            "chat_id": ADMIN_ID,
            "text": f"رسالة جديدة:\n{text}"
        })

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
