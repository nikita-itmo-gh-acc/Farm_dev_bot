import telebot as tb
from db_create import cursor, farm_dev_db
from text_data import reg_dict
name, email, phone = '', '', ''
seller = False


def register(message, bot):
    global seller
    if message.text == "/reg":
        bot.send_message(message.from_user.id, reg_dict["reg"])
        bot.register_next_step_handler(message, get_user_name, bot)
    elif message.text == "/reg_sell":
        bot.send_message(message.from_user.id, reg_dict["reg"])
        seller = True
        bot.register_next_step_handler(message, get_user_name, bot)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, reg_dict["help"])
    elif message.text == "/info":
        bot.send_message(message.from_user.id, reg_dict["info"])
    else:
        bot.send_message(message.from_user.id, reg_dict["unknown"])


def get_user_name(message, bot):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Укажите адрес электронной почты')
    bot.register_next_step_handler(message, get_email, bot)


def get_email(message, bot):
    global email
    email = message.text
    if seller:
        bot.send_message(message.from_user.id, 'Укажите номер телефона')
        bot.register_next_step_handler(message, get_phone_number, bot)
    else:
        get_save_access(message.from_user.id, bot)


def get_phone_number(message, bot):
    global phone
    phone = message.text
    get_save_access(message.from_user.id, bot)


def get_save_access(user_id, bot):
    keyboard = tb.types.InlineKeyboardMarkup()
    key_yes = tb.types.InlineKeyboardButton(text='Да', callback_data='yes')
    key_no = tb.types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no, key_yes)
    question = 'Сохранить ваши данные?'
    bot.send_message(user_id, text=question, reply_markup=keyboard)


def callback_worker(call, bot):
    global name, email
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Данные сохранены')
        save_data()
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Данные будут удалены по завершении сессии')


def save_data():
    global seller
    cursor.execute("USE sql7707767")
    if seller:
        cursor.execute(f"""INSERT INTO Sellers (name, email, phone) VALUES ('{name}', '{email}', '{phone}')""")
    else:
        cursor.execute(f"""INSERT INTO Users (name, email) VALUES ('{name}', '{email}')""")
    farm_dev_db.commit()
