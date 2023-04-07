import telegram
import os

TOKEN=os.environ.get("TOKEN")
url = "https://flaskapp2023.pythonanywhere.com/webhook"
bot = telegram.Bot(TOKEN)

# print(bot.delete_webhook())

# print(bot.set_webhook(url))
print(bot.get_webhook_info())