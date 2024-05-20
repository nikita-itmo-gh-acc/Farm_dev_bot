import telebot as tb
from db_create import cursor, farm_dev_db
name, email = '', ''


def register(message, bot):
    if message.text == "/reg":
        bot.send_message(message.from_user.id, "Привет, напишите пожалуйста как вас зовут")
        bot.register_next_step_handler(message, get_user_name, bot)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Для начала регистрации напишите /reg, \
                                                    для регистрации продавца напишите  \
                                                    для получения \
                                                    информации о боте напишите /info")
    else:
        bot.send_message(message.from_user.id, "Неизвестное сообщение, напишите /help для просмотра возможных \
                                                    сообщений")


def get_user_name(message, bot):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Укажите адрес электронной почты')
    bot.register_next_step_handler(message, get_save_access, bot)


def get_save_access(message, bot):
    global email
    email = message.text
    keyboard = tb.types.InlineKeyboardMarkup()
    key_yes = tb.types.InlineKeyboardButton(text='Да', callback_data='yes')
    key_no = tb.types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no, key_yes)
    question = 'Сохранить ваши данные?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


def callback_worker(call, bot):
    global name, email
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Данные сохранены')
        cursor.execute("USE FarmDB")
        cursor.execute(f"""INSERT INTO Users (name, email) VALUES ('{name}', '{email}')""")
        farm_dev_db.commit()
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Данные будут удалены по завершении сессии')

