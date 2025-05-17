import json
from handlers.conversation.generate_template import generate_template_data_handler
from handlers import state_handler, data_handler

state = state_handler.state

def register_callback(bot):
    @bot.callback_query_handler()
    def handler(call):
        chat_id = call.from_user.id
        data = json.loads(call.data)

        if not chat_id in state:
            bot.answer_callback_query(call.id)
            bot.send_message(chat_id, 'Harap /start dulu.')
            return

        conversation = state[chat_id]['conversation']

        if conversation == 'welcome':
            data_handler.callback_handler(chat_id, data, bot)
        elif conversation == 'generate_template':
            generate_template_data_handler.callback_handler(chat_id, data, bot)

        bot.answer_callback_query(call.id)

