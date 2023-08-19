import logging
from telegram import ForceReply, Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
from message_handlers import handle_message, delete_user_history, start_session
from Utils.consts import TELEGRAM_TOKEN


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id_str = str(update.effective_user.id)
    return_message = start_session(user_id_str)

    await update.message.reply_text(return_message)


async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id_str = str(update.effective_user.id)
    return_message = delete_user_history(user_id_str)
    await update.message.reply_text(return_message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help!")


async def get_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id_str = str(update.effective_user.id)
    return_message, ans_options = handle_message(user_id_str, update.message.text)

    reply_markup = await create_inline_keyboard_from_list(ans_options) if ans_options else None

    await update.message.reply_text(return_message, reply_markup=reply_markup)


async def get_answer_btn(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id_str = str(update.effective_user.id)
    user_ans = update.callback_query['data']
    return_message, ans_options = handle_message(user_id_str,  user_ans)

    reply_markup = await create_inline_keyboard_from_list(ans_options) if ans_options else None

    await update.callback_query.message.reply_text(return_message, reply_markup=reply_markup)


async def create_inline_keyboard_from_list(options: list[str]):
    keyboard = [[InlineKeyboardButton(option, callback_data=option)] for option in options]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("clear", clear_command))
    application.add_handler(CallbackQueryHandler(get_answer_btn))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_message))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
