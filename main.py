import telebot as tb
from db_create import create_db
from registration import *
farm_bot = tb.TeleBot('6813586303:AAHwBwwUL7AmCy5RFjkyJrUI49Tl-OkXpOk')


def main():
    farm_bot.register_message_handler(register, pass_bot=True)
    farm_bot.register_callback_query_handler(callback_worker, func=lambda call: True,  pass_bot=True)
    farm_bot.polling(none_stop=True, interval=0)


if __name__ == "__main__":
    # create_db()
    main()
