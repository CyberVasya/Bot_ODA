import logging

from telebot import TeleBot
from telebot.types import Message

from bot.callbacks import variants_callback
from bot.keyboard import regions_markup, variants_markup, regions
from bot.utils import is_message_valid
from orm.controllers import init_user, save_user_answer
from settings import VARIANT_REPLY, BACK_ACTION


def start_handler(message: Message, bot: TeleBot) -> None:
    """Хендлер для команды /start"""
    logging.warning(f'Start command received from {message.from_user.id}')

    bot.send_message(
        message.chat.id,
        "Доброго дня,{0.first_name}👋\n🔍Оберіть Громаду 🏡 :".format(message.from_user),
        reply_markup=regions_markup
    )
    init_user(message)


def text_handler(message: Message, bot: TeleBot) -> None:
    """Хендлер для текстовых сообщений"""
    logging.warning(f'Handling text content type from user {message.from_user.id}')

    if is_message_valid(message, mapping=regions):
        save_user_answer(message, region=message.text)
        bot.send_message(message.from_user.id, VARIANT_REPLY, reply_markup=variants_markup)
        bot.register_next_step_handler(
            message, variants_callback, bot=bot, start_handler=start_handler, text_handler=text_handler)

    if message.text == BACK_ACTION:
        bot.send_message(message.from_user.id, VARIANT_REPLY, reply_markup=variants_markup)
        bot.register_next_step_handler(
            message, variants_callback, bot=bot, start_handler=start_handler, text_handler=text_handler)
