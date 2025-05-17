from dotenv import load_dotenv
import os

#load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
USER_CHAT_ID = int(os.getenv('USER_CHAT_ID'))
PATH = '/webhook'
WEBHOOK_URL = os.getenv('WEBHOOK_URL') + PATH