import telebot as tb
from db_create import cursor, farm_dev_db
phone, link = '', ''


def get_phone_number(message, bot):
    global phone
    phone = message.text
    site_link_choice(message.from_user.id, bot)


def get_site_link(message, bot):
    global link
    link = message.text
    get_save_access(message.from_user.id, bot)


def get_save_access(user_id, bot):
    keyboard = tb.types.InlineKeyboardMarkup()
    key_save = tb.types.InlineKeyboardButton(text='💾 Сохранить', callback_data='save')
    key_delete = tb.types.InlineKeyboardButton(text='💁‍♂️ Забыть', callback_data='delete')
    keyboard.add(key_save, key_delete)
    question = 'Сохранить ваши данные?'
    bot.send_message(user_id, text=question, reply_markup=keyboard)


def callback_worker_link(call, bot):
    if call.data == "remain":
        bot.send_message(call.message.chat.id, 'Вставьте ссылку на ваш сайт')
        bot.register_next_step_handler(call.message, get_site_link, bot)
    elif call.data == "skip":
        bot.send_message(call.message.chat.id, 'Ссылку можно прикрепить позже')
        get_save_access(call.message.chat.id, bot)


def site_link_choice(user_id, bot):
    keyboard = tb.types.InlineKeyboardMarkup()
    key_remain = tb.types.InlineKeyboardButton(text='✅ Да', callback_data='remain')
    key_skip = tb.types.InlineKeyboardButton(text='❌ Нет', callback_data='skip')
    keyboard.add(key_remain, key_skip)
    question = 'Оставить ссылку на ваш сайт?'
    bot.send_message(user_id, text=question, reply_markup=keyboard)


def get_extra_data():
    return phone, link
