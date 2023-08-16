from typing import List
from dotenv import load_dotenv
import requests
from flask import Flask, request
from requests import Response
import os

load_dotenv()
OPENAI_TOKEN: str = os.getenv('OPENAI_TOKEN')
TELEGRAM_TOKEN: str = os.getenv('TELEGRAM_TOKEN')
NGROK_FORWARDING: str = os.getenv('NGROK_FORWARDING')
TELEGRAM_INIT_WEBHOOK_URL: str = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/setWebhook?url={NGROK_FORWARDING}'

app: Flask = Flask(__name__)


@app.route('/message', methods=["POST"])
def handle_message() -> str:
    if 'message' in request.get_json():
        chat_id: str = request.get_json()['message']['chat']['id']
        my_message: List[str] = request.get_json()['message']['text'].strip().split(' ')
    elif 'edited_message' in request.get_json():
        chat_id: str = request.get_json()['edited_message']['chat']['id']
        my_message: List[str] = request.get_json()['edited_message']['text'].strip().split(' ')
    else:
        return "Error"

    text_response: str = my_message[0]

    res: Response = requests.get(
        f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={text_response}')

    return "success" if res.ok else "Error"


if __name__ == '__main__':
    requests.get(TELEGRAM_INIT_WEBHOOK_URL)
    app.run(port=5002, debug=True)
