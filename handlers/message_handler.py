from handlers.conversation.generate_template import generate_template_data_handler
from utils import markup_utils
from handlers import state_handler


def welcome_handler(chat_id, bot):
    bot.send_message(chat_id, 'Selamat datang di Nuts Bot, silahkan pilih fungsi dibawah ini', reply_markup=markup_utils.get_welcome_markup())
    state_handler.state[chat_id] = {'conversation': 'welcome'}

    #generate_template_conversation.start(message.chat.id, bot)

def register_handler(bot):
    @bot.message_handler(commands=['start'])
    def handler(message):
        print('Detected')
        welcome_handler(message.chat.id, bot)

    @bot.message_handler(func=lambda message: True)
    def handle_all_message(message):
        if message.from_user.is_bot:
            return
        
        if message.chat.id not in state_handler.state:
            bot.send_message(message.chat.id, 'Harap /start dulu')
            return

        if state_handler.state[message.chat.id]['conversation'] == 'generate_template':
            generate_template_data_handler.message_handler(message.chat.id, bot)