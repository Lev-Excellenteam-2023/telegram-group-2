from typing import List
from Utils.consts import *
import requests
from flask import Flask, request
from requests import Response
from Database.firebase_db import DatabaseManager

app: Flask = Flask(__name__)


@app.route('/message', methods=["POST"])
def handle_message() -> str:
    if 'message' in request.get_json():
        chat_id: str = str(request.get_json()['message']['chat']['id'])
        my_message: List[str] = request.get_json()['message']['text'].strip().split(' ')
    else:
        return "Error"

    if not database_instance.is_user_exist(chat_id):
        database_instance.insert_user(chat_id)

    text_response: str = my_message[0]

    res: Response = requests.get(
        f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={text_response}')

    database_instance.add_message_to_user(chat_id, my_message[0], text_response)

    return "success" if res.ok else "Error"


if __name__ == '__main__':
    requests.get(TELEGRAM_INIT_WEBHOOK_URL)
    database_instance: DatabaseManager = DatabaseManager()
    app.run(port=5002, debug=True)
