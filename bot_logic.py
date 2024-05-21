import telebot as tb
from text_data import reg_dict
from registration import *
from auth import *

seller = False


def auth(message, bot):
    bot.send_message(message.from_user.id, reg_dict["auth"])
    bot.register_next_step_handler(message, check_email, bot)


def reg(message, bot):
    bot.send_message(message.from_user.id, reg_dict["reg"])
    bot.register_next_step_handler(message, get_user_name, bot)


def reg_sell(message, bot):
    global seller
    bot.send_message(message.from_user.id, reg_dict["reg"])
    seller = True
    bot.register_next_step_handler(message, get_user_name, bot, seller)


def info(message, bot):
    bot.send_message(message.from_user.id, reg_dict["info"])


def help_func(message, bot):
    bot.send_message(message.from_user.id, reg_dict["help"])


def default(message, bot):
    bot.send_message(message.from_user.id, reg_dict["unknown"])


switch = {
    "/reg": reg, "/reg_sell": reg_sell, "/info": info, "/help": help_func, "/auth": auth
}


def main_start(message, bot):
    global switch
    switch.get(message.text, default)(message, bot)
