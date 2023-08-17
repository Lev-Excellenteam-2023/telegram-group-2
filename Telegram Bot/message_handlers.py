import logging
from Database.firebase_db import DatabaseManager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

USER_DB = DatabaseManager()


def handle_message(user_id: str, msg_text: str):
    logger.info(f"Handling message for user {user_id}")
    check_or_create_user(user_id)
    USER_DB.add_message_to_user(user_id, msg_text, 'response')

    return "db ok"


def check_or_create_user(user_id: str):
    if not USER_DB.is_user_exist(user_id):
        USER_DB.insert_user(user_id)
        logger.info(f"Created new user: {user_id}")


def delete_user_history(user_id: str):
    try:
        USER_DB.delete_user(user_id)
        logger.info(f"Deleted user history for user: {user_id}")
    except ValueError as e:
        error_msg = e.args[0]
        logger.error(f"Error deleting user history for user {user_id}: {error_msg}")
        return error_msg

    return 'history deleted'
