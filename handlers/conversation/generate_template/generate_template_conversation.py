from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from handlers.conversation.generate_template import generate_template
import json, config
from handlers import state_handler

state = state_handler.state

def start(chat_id, bot):
    state[chat_id] = {'conversation': 'generate_template'}
    ask_account_type(chat_id, bot)

def ask_account_type(chat_id, bot):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton('SSH', callback_data=json.dumps({'type': 'account_type', 'account_type': 'ssh'})),
        InlineKeyboardButton('VMESS', callback_data=json.dumps({'type': 'account_type', 'account_type': 'vmess'})),
        InlineKeyboardButton('VLESS', callback_data=json.dumps({'type': 'account_type', 'account_type': 'vless'})),
        InlineKeyboardButton('TROJAN', callback_data=json.dumps({'type': 'account_type', 'account_type': 'trojan'})),
        InlineKeyboardButton('Back', callback_data=json.dumps({'type': 'back'}))
    )

    bot.send_message(chat_id, 'Silahkan pilih tipe akun.', reply_markup=markup)

def ask_name(chat_id, bot):
    state[chat_id]['type'] = 'name'

    bot.send_message(chat_id, 'Masukkan username akun vpn :')

def ask_expired(chat_id, bot):
    state[chat_id]['type'] = 'expired'
    
    bot.send_message(chat_id, 'Silahkan masukkan expired (day) : ')

def ask_password(chat_id, bot):
    state[chat_id]['type'] = 'password'

    bot.send_message(chat_id, 'Masukkan Password ( Jika v2ray, masukkan UUID ) :')

def ask_max_device(chat_id, bot):
    state[chat_id]['type'] = 'max_device'

    bot.send_message(chat_id, 'Max Device : ')

def ask_host(chat_id, bot):
    state[chat_id]['type'] = 'host'

    bot.send_message(chat_id, 'Masukkan host VPN ( d for Default ) :')

def ask_provider(chat_id, bot):
    state[chat_id]['type'] = 'provider'

    bot.send_message(chat_id, 'Masukkan provider VPN ( d for Default ) :')

def generate(chat_id, bot):
    transaction_template = generate_template.generate(state[chat_id])

    if chat_id == config.USER_CHAT_ID:
        bot.send_message(chat_id, transaction_template, parse_mode='HTML')
    else:
        bot.send_message(chat_id, 'Bro 😂, yakali admin tidak memblok akses ini jir.')

    state.pop(chat_id)
