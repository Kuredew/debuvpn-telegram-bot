from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import json

def get_welcome_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton('TRX Template Generator', callback_data=json.dumps({'tool': 'trx_template_generator'})),
    )

    return markup

