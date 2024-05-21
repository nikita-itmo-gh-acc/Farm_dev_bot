from db_create import cursor, farm_dev_db


def check_email(message, bot):
    cursor.execute("USE sql7707767")
    cursor.execute(f"SELECT * FROM Users WHERE email = '{message.text}';")
    found = cursor.fetchone()
    if len(found) == 1:
        bot.send_message(message.from_user.id, "Авторизация прошла успешно")
        bot.register_next_step_handler(message, make_user_choice, bot)
    else:
        bot.send_message(message.from_user.id, "Пользователя с таким email нет в системе")


def make_user_choice(message, bot):
    pass
