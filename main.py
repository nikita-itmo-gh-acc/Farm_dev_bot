import telebot as tb
from db_create import create_db
from bot_logic import *
from reg_sellers import callback_worker_link

farm_bot = tb.TeleBot('6813586303:AAHwBwwUL7AmCy5RFjkyJrUI49Tl-OkXpOk')


def main():
    farm_bot.register_message_handler(main_start, pass_bot=True)
    farm_bot.register_callback_query_handler(callback_worker_save, func=lambda call:
                                             call.data == "save" or call.data == "delete", pass_bot=True)
    farm_bot.register_callback_query_handler(callback_worker_link, func=lambda call:
                                             call.data == "remain" or call.data == "skip", pass_bot=True)
    farm_bot.polling(none_stop=True, interval=0)


if __name__ == "__main__":
    # create_db()
    main()
