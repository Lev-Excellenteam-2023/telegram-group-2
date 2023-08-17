import logging
from telegram import ForceReply, Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from message_handlers import handle_message, delete_user_history, start_session
from Utils.consts import TELEGRAM_TOKEN


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id_str = str(update.effective_user.id)
    return_message = start_session(user_id_str)
    reply_keyboard = [["Boy", "Girl", "Other"]]

    await update.message.reply_text(return_message, reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=False, resize_keyboard=True, input_field_placeholder="Boy or Girl?"
    ))

    reply_keyboard = [["Boy", "Girl", "Other"]]


async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id_str = str(update.effective_user.id)
    return_message = delete_user_history(user_id_str)
    await update.message.reply_text(return_message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help!")


async def get_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id_str = str(update.effective_user.id)
    return_message = handle_message(user_id_str, update.message.text)

    await update.message.reply_text(return_message)


def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("clear", clear_command))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_message))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
