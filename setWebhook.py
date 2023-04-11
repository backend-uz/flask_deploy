import telegram

TOKEN="1950937652:AAEKFVSEwjT55RYro5X-3ILwKXnh_s6ThPU"
url = "https://bacefap.pythonanywhere.com/webhook"
bot = telegram.Bot(TOKEN)

# print(bot.delete_webhook())

print(bot.set_webhook(url))
# print(bot.get_webhook_info())