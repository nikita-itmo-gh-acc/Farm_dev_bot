import telebot as tb
from db_create import cursor, farm_dev_db
from reg_sellers import get_phone_number, get_save_access, get_extra_data
name, email = '', ''
sell = False


def get_user_name(message, bot, seller=False):
    global name, sell
    sell = seller
    name = message.text
    bot.send_message(message.from_user.id, 'Укажите адрес электронной почты')
    bot.register_next_step_handler(message, get_email, bot)


def get_email(message, bot):
    global email
    email = message.text
    if sell:
        bot.send_message(message.from_user.id, 'Укажите номер телефона')
        bot.register_next_step_handler(message, get_phone_number, bot)
    else:
        get_save_access(message.from_user.id, bot)


def callback_worker_save(call, bot):
    global name, email
    if call.data == "save":
        bot.send_message(call.message.chat.id, 'Данные сохранены')
        save_data()
    elif call.data == "delete":
        bot.send_message(call.message.chat.id, 'Данные будут удалены по завершении сессии')


def save_data():
    cursor.execute("USE sql7707767")
    phone, link = get_extra_data()
    if sell:
        cursor.execute(f"""INSERT INTO Sellers (name, email, phone, site_link) \
        VALUES ('{name}', '{email}', '{phone}', '{link}')""")
    else:
        cursor.execute(f"""INSERT INTO Users (name, email) VALUES ('{name}', '{email}')""")
    farm_dev_db.commit()
