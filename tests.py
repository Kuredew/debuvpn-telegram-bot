import requests

my_bot_token = '698990035:AAHNgwLUdWDBoFEOrkoYnIxbUNHxB4vGEfY'
url_to_send_updates_to = 'https://hibiku.pythonanywhere.com/'
url = f'https://api.telegram.org/bot{my_bot_token}/setWebhook?url={url_to_send_updates_to}'

r = requests.post('https://hibiku.pythonanywhere.com/')

print(r.json())