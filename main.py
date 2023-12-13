import telebot
from datetime import datetime

bot = telebot.TeleBot('6580829810:AAG7h5nLRt-8lWriPZf7423Vq3B5ZTZYSZM')
to_do_list = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!"
                                      "\nЧтобы добавить новый дедлайн, введите сообщение в формате "
                                      "<b>Название дедлайна : ГГГГ-ММ-ДД</b>"
                                      "\nЧтобы посмотреть список всех ваших дедлайнов,"
                                      " введите команду /show_all_deadlines "
                                      "или напишите <i>Вывести список дедлайнов</i>"
                                      "\nЧтобы удалить прошедшие даты введите команду /delete "
                                      "или напишите <i>Списать просрочку</i>", parse_mode='html')


@bot.message_handler(commands=['show_all_deadlines'])
def show_all_deadlines(message):
    if len(to_do_list) == 0:
        bot.send_message(message.chat.id, "Ваш список пуст")
    else:
        sorti = dict(sorted(to_do_list.items()))
        for key in sorti:
            bot.send_message(message.chat.id, f'{key} :')
            for dedl in to_do_list[key]:
                bot.send_message(message.chat.id, f"- {dedl}")


@bot.message_handler(commands=['delete'])
def delete(message):
    today = datetime.today().date()
    keys_to_delite = []
    for key in list(to_do_list):
        if key < today:
            keys_to_delite.append(key)
    if len(keys_to_delite) == 0:
        bot.send_message(message.chat.id, "Данные списка дедлайнов актуальны")
    else:
        for kkey in keys_to_delite:
            del to_do_list[kkey]
        bot.send_message(message.chat.id, f"Просрочка списана")


@bot.message_handler(content_types=['text'])
def add_reminder(message):
    texti = message.text.lower()
    if texti == 'вывести список дедлайнов':
        show_all_deadlines(message)
    elif texti == 'списать просрочку':
        delete(message)
    else:
        try:
            task_text, task_date = message.text.split(':')
            task_date = task_date.replace(' ', '')
            task_date = datetime.strptime(task_date, '%Y-%m-%d').date()
            if task_date in to_do_list:
                to_do_list[task_date].append(task_text)
            else:
                to_do_list[task_date] = list()
                to_do_list[task_date].append(task_text)
            bot.send_message(message.chat.id, f"Напоминание '{task_text}' добавлено на {task_date}")
        except Exception:
            bot.send_message(message.chat.id, "Бот не распознал ваш формат сообщения!")


bot.polling(none_stop=True)
