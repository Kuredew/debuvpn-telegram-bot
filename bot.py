import telebot
import config
from flask import Flask, request

from handlers import message_handler, callback_handler

bot = telebot.TeleBot(config.BOT_TOKEN)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    json = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json)

    bot.process_new_updates([update])
    return 'ok', 200

message_handler.register_handler(bot)
callback_handler.register_callback(bot)


print('Bot Started.')