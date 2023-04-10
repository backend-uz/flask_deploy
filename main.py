from flask import Flask, request
import os
import telegram

TOKEN = "5661659754:AAGS37bnekJLOCeHHvmh2KdIOo8uNZG_kyM"

bot = telegram.Bot(TOKEN)

app = Flask(__name__)

@app.route("/api")
def main():
    return "DEPLYMENT"

@app.route("/webhook", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        print(request.get_json())
        chat_id = 5575549228
        bot.sendMessage(chat_id, "Hello, 123")

        return "send Message"
    else:
        return "Not allowed GET request"
    

if __name__ == "__main__":
    app.run(debug=True)