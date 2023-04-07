from telegram.ext import Dispatcher, Updater, CommandHandler, MessageHandler, Filters
from handlers import start, echo
import os

TOKEN=os.environ.get("TOKEN")

updater = Updater(token=TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
updater.idle()