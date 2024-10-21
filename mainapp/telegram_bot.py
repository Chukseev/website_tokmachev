import requests
from decouple import config, Csv
import os


def send_telegram_message(name, email, message):
    bot_token = config('BOT_TOKEN')
    chat_id = config('CHAT_ID')

    text = f"Вам отправили сообшение:\n\nName: {name}\nEmail: {email}\nMessage: {message}"

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    response = requests.post(url, data=payload)

    return response.status_code
