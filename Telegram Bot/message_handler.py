from Database.firebase_db import DatabaseManager

USER_DB = DatabaseManager()


def handle_message(user_id: str, msg_text: str):
    check_or_create_user(user_id)
    USER_DB.add_message_to_user(user_id, msg_text, 'response')

    return "db ok"


def check_or_create_user(user_id: str):
    if not USER_DB.is_user_exist(user_id):
        USER_DB.insert_user(user_id)


