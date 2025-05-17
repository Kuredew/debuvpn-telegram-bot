from handlers.conversation.generate_template import generate_template_conversation

def callback_handler(chat_id, data, bot):
    tool = data['tool']

    if tool == 'trx_template_generator':
        generate_template_conversation.start(chat_id, bot)
