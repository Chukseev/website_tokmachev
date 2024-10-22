import requests
from decouple import config


def send_telegram_message(name, email, message, phone):
    bot_token = config('BOT_TOKEN')
    chat_id = config('CHAT_ID')

    text = f"Вам отправили сообшение:\n\nИмя: {name}\nEmail: {email}\nPhone: {phone}\nСообщение: {message}"

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    response = requests.post(url, data=payload)

    return response.status_code
