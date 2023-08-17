from typing import List
import firebase_admin
from firebase_admin import credentials, db
from firebase_admin.credentials import Certificate
from firebase_admin.db import Reference
import time
from Utils.consts import DATABASE_URL


class DatabaseManager:
    users_ref: Reference

    def __init__(self):
        cred: Certificate = credentials.Certificate("./serviceAccountKey.json")
        firebase_admin.initialize_app(cred, options={
            'databaseURL': f'{DATABASE_URL}'
        })

        self.users_ref = db.reference('users')

    def insert_user(self, chat_id: str) -> None:
        if not chat_id.isdigit():
            raise ValueError('chat_id must be a number')

        if self.is_user_exist(chat_id):
            raise ValueError('User already exist')

        user_ref = self.users_ref.child(chat_id).child('conversation')
        user_ref = user_ref.push({'message': 'user initialization', 'timestamp': int(time.time() * 1000)})
        user_ref.child('response').set({'message': 'telegram bot initialization'})

    def is_user_exist(self, chat_id: str) -> bool:
        return True if self.users_ref.child(chat_id).get() is not None else False

    def add_message_to_user(self, chat_id: str, message: str, response: str) -> None:
        if not self.is_user_exist(chat_id):
            raise ValueError('User does not exist')
        user_ref = self.users_ref.child(chat_id)
        conversation_ref = user_ref.child('conversation')

        new_message_ref = conversation_ref.push()
        new_message_ref.set({'message': message, 'timestamp': int(time.time() * 1000)})

        new_response_ref = new_message_ref.child('response')
        new_response_ref.set({'message': response})

    def get_conversation_history(self, chat_id: str) -> List:
        if not self.is_user_exist(chat_id):
            raise ValueError('User does not exist')

        user_ref = self.users_ref.child(chat_id)
        conversation_ref = user_ref.child('conversation')

        conversation_snapshot = conversation_ref.get()

        sorted_messages = sorted(
            conversation_snapshot.values(),
            key=lambda x: x.get('timestamp', 0)
        )

        return sorted_messages


if __name__ == '__main__':
    # testing
    my_db: DatabaseManager = DatabaseManager()
    my_db.insert_user('1234567890')
    # my_db.add_message_to_user('1234567890', 'test', '123')
    # print(my_db.get_conversation_history('1234567890'))
