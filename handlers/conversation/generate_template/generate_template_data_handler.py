from handlers.conversation.generate_template import generate_template_conversation
from handlers import state_handler, lobby_handler

state = state_handler.state

def callback_handler(chat_id, data, bot):
    type = data['type']


    if type == 'account_type':
        state[chat_id]['account_type'] = data['account_type']

        generate_template_conversation.ask_name(chat_id, bot)
    elif type == 'back':
        lobby_handler.welcome_handler(chat_id, bot)

def message_handler(chat_id, text, bot):

    if state[chat_id]['type'] == 'name':
        state[chat_id]['name'] = text

        generate_template_conversation.ask_expired(chat_id, bot)
    elif state[chat_id]['type'] == 'expired':
        state[chat_id]['expired'] = text

        generate_template_conversation.ask_password(chat_id, bot)
    elif state[chat_id]['type'] == 'password':
        state[chat_id]['password'] = text

        generate_template_conversation.ask_max_device(chat_id, bot)
    elif state[chat_id]['type'] == 'max_device':
        state[chat_id]['max_device'] = text

        generate_template_conversation.ask_host(chat_id, bot)
    elif state[chat_id]['type'] == 'host':
        if text == 'd':
            state[chat_id]['host'] = 'do.fiuzeanet.my.id'
        else:
            state[chat_id]['host'] = text

        generate_template_conversation.ask_provider(chat_id, bot)
    elif state[chat_id]['type'] == 'provider':
        if text == 'd':
            state[chat_id]['provider'] = 'SG DigitalOcean'
        else:
            state[chat_id]['provider'] = text

        generate_template_conversation.generate(chat_id, bot)
