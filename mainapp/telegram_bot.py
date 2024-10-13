import requests


def send_telegram_message(name, email, message):
    bot_token = ''  # Ваш токен бота
    chat_id = ''  # Ваш Chat ID (ID чата, куда нужно отправить сообщение)

    text = f"Вам отправили сообшение:\n\nName: {name}\nEmail: {email}\nMessage: {message}"

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    response = requests.post(url, data=payload)

    return response.status_code
