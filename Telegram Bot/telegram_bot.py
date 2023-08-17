import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
from os import getenv
from message_handler import handle_message

load_dotenv()

TOKEN = getenv('TELEGRAM_TOKEN')

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    user_id_str = str(update.effective_user.id)
    return_massege = handle_message(user_id_str, update.message.text)

    await update.message.reply_text(return_massege)


def main() -> None:

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()