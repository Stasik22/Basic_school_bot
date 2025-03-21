import time
import telebot as tb

from datetime import datetime
from Notes import  notes_save
from Notes import  notes_data
from Buttons import start_button_func, schedule_buttons, notes_button
from Buttons import class_num
from Schedule import scheule_11C
from Buttons import des
from Buttons import site_buttons
from Buttons import app_buttons

API_TOKEN = ''
bot = tb.TeleBot(API_TOKEN)

@bot.message_handler(commands=["Нотатки"])
def notes(message):
    chat_id = str(message.chat.id)
    user_notes = notes_data.get(chat_id, [])

    if isinstance(user_notes, list):
        notes_text = "\n".join(f"{i + 1}. {note.get('text', 'Невідома нотатка')} (📅 {note.get('date', 'Невідома дата')})" for i, note in enumerate(user_notes) if isinstance(note, dict))
        bot.send_message(chat_id, f"f<b>Ваші нотатки</b>\n{notes_text}" if notes_text else "<b>У вас ще немає нотаток</b>", parse_mode="html" ,reply_markup=notes_button())
    else:
        bot.send_message(chat_id, "<b>Помилка формату нотаток</b>", parse_mode="html", reply_markup=notes_button())


@bot.message_handler(commands=["Створити"])

def create_note(message):
    bot.send_message(message.chat.id, "<b>Напишіть вашу нотатку:</b>", parse_mode="html")
    bot.register_next_step_handler(message, save_note)

def  save_note(message):
    chat_id = str(message.chat.id)
    note_text = message.text.strip()

    if note_text:
        note_entry = {"text": note_text, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        notes_data.setdefault(chat_id, []).append(note_entry)
        notes_save(notes_data)
        bot.send_message(chat_id, "✅ Нотатку збережено!", parse_mode="html", reply_markup=notes_button())
    else:
        bot.send_message(chat_id, "❌ Нотатка не може бути порожньою!", parse_mode="html")

@bot.message_handler(commands=["Очистити"])
def clear_notes(message):
    chat_id = str(message.chat.id)
    if chat_id in notes_data:
        del notes_data[chat_id]
        notes_save(notes_data)
        bot.send_message(chat_id, "🗑️<b>Немає нотаток,оскільки всі нотатки видалені</b>",parse_mode="html", reply_markup=notes_button())
    else:
        bot.send_message(chat_id, "❗<b>У️ вас немає нотаток для видалення</b>", parse_mode="html")
    pass

@bot.message_handler(commands=["Подивитись"])
def view_notes(message):
    chat_id = str(message.chat.id)
    user_notes = notes_data.get(chat_id, [])

    if isinstance(user_notes, list):
        notes_text = "\n".join(f"{i + 1}. {note.get('text', 'Невідома нотатка')} (📅 {note.get('date', 'Невідома дата')})" for i, note in enumerate(user_notes) if isinstance(note, dict))
        bot.send_message(chat_id, f"<b>Ваші нотатки:</b>\n{notes_text}" if notes_text else "<b>У вас ще немає нотаток.</b>",parse_mode="html")
    else:
        bot.send_message(chat_id,"<b>‽Помилка в форматі нотаток</b>",reply_markup=notes_button(), parse_mode="html")
    return view_notes


@bot.message_handler(commands=['Сайт'])
def site(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "<b>Натисніть щоб відкрити сайт</b>",parse_mode="html",  reply_markup=site_buttons())

@bot.message_handler(commands=["Додаток"])
def app (message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "<b>Ось наш додаток.Виберіть ОС якою ви користуєтесь задля подальшого відвідання додатку</b>", parse_mode="html", reply_markup = app_buttons())

@bot.message_handler(commands=["start"])
def start_function(message):
    bot.send_message(message.chat.id, "<b>Всіх вітаю!Це офіційний телеграм бот 5 школи.</b>", parse_mode="html",reply_markup=start_button_func())

@bot.message_handler(commands=["Домашня"])
def homework(message):
    bot.send_message(message.chat.id, "Ось ваше домашнє завдання", parse_mode="html")


@bot.message_handler(commands=["Розклад"])
def Schedule_function(message):
    bot.send_message(message.chat.id,"<b>Оберіть ваш клас з поданих нижче,щоб отримати свій розклад</b>",parse_mode="html",reply_markup=schedule_buttons())

@bot.message_handler(commands=["11_класи"])
def eleventh(message):
    chat_id = message.chat.id
    bot.send_message(message.chat.id,"<b>Оберіть літеру вашого класу</b>", parse_mode="html", reply_markup=class_num())
    @bot.message_handler(commands=["А"])
    def A_class(message):
        bot.send_message(chat_id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>", reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Б"])
    def B_class(message):
        bot.send_message(chat_id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>", reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["В"])
    def C_class(message):
        bot.send_message(chat_id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Г"])
    def G_class(message):
        bot.send_message(chat_id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Текст"])
    def text_message(message):
        bot.send_message(chat_id, scheule_11C, parse_mode="html")
        time.sleep(1)
        bot.send_message(chat_id, "<b>Оберіть функцію з поданих нижче</b>", reply_markup=start_button_func(),parse_mode="HTML")
    pass

    @bot.message_handler(commands=["Фото"])
    def photo(message):
        with open("/Users/stasuk2007/Documents/istockphoto-525430193-612x612.jpg", "rb") as file:
            bot.send_photo(message.chat.id, file)
            time.sleep(1)
            bot.send_message(chat_id, "<b>Оберіть функцію з поданих нижче</b>",reply_markup=start_button_func(), parse_mode="HTML")
        pass
    pass


@bot.message_handler(commands=["10_класи"])
def tenth(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "<b>Оберіть літеру вашого класу</b>", parse_mode="html", reply_markup=class_num())

    @bot.message_handler(commands=["А"])
    def A_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Б"])
    def B_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["В"])
    def C_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Г"])
    def G_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Текст"])
    def text_message(message):
        bot.send_message(message.chat.id, scheule_11C, parse_mode="html")
        time.sleep(1)
        bot.send_message(message.chat.id, "<b>Оберіть функцію з поданих нижче</b>", reply_markup=start_button_func(),parse_mode="HTML")
    pass

    @bot.message_handler(commands=["Фото"])
    def photo(message):
        with open("/Users/stasuk2007/Documents/istockphoto-525430193-612x612.jpg", "rb") as file:
            bot.send_photo(message.chat.id, file)
            time.sleep(1)
            bot.send_message(message.chat.id, "<b>Оберіть функцію з поданих нижче</b>",reply_markup=start_button_func(), parse_mode="HTML")
        pass
    pass


@bot.message_handler(commands=["9_класи"])
def ninths(message):
    bot.send_message(message.chat.id, "<b>Оберіть літеру вашого класу</b>", parse_mode="html", reply_markup=class_num())

    @bot.message_handler(commands=["А"])
    def A_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")

    pass

    @bot.message_handler(commands=["Б"])
    def B_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")

    pass

    @bot.message_handler(commands=["В"])
    def C_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Г"])
    def G_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Текст"])
    def text_message(message):
        bot.send_message(message.chat.id, scheule_11C, parse_mode="html")
        time.sleep(1)
        bot.send_message(message.chat.id, "<b>Оберіть функцію з поданих нижче</b>", reply_markup=start_button_func(),parse_mode="HTML")
    pass

    @bot.message_handler(commands=["Фото"])
    def photo(message):
        with open("/Users/stasuk2007/Documents/istockphoto-525430193-612x612.jpg", "rb") as file:
            bot.send_photo(message.chat.id, file)
            time.sleep(1)
            bot.send_message(message.chat.id, "<b>Оберіть функцію з поданих нижче</b>",reply_markup=start_button_func(), parse_mode="HTML")
        pass
    pass

@bot.message_handler(commands=["8_класи"])
def eighths(message):
    bot.send_message(message.chat.id, "<b>Оберіть літеру вашого класу</b>", parse_mode="html", reply_markup=class_num())

    @bot.message_handler(commands=["А"])
    def A_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Б"])
    def B_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["В"])
    def C_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Г"])
    def G_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Текст"])
    def text_message(message):
        bot.send_message(message.chat.id, scheule_11C, parse_mode="html")
        time.sleep(1)
        bot.send_message(message.chat.id, "<b>Оберіть функцію з поданих нижче</b>", reply_markup=start_button_func(), parse_mode="HTML")
    pass

    @bot.message_handler(commands=["Фото"])
    def photo(message):
        with open("/Users/stasuk2007/Documents/istockphoto-525430193-612x612.jpg", "rb") as file:
            bot.send_photo(message.chat.id, file)
            time.sleep(1)
            bot.send_message(message.chat.id, "<b>Оберіть функцію з поданих нижче</b>",reply_markup=start_button_func(), parse_mode="HTML")
        pass
    pass

@bot.message_handler(commands=["7_класи"])
def seventh(message):
    bot.send_message(message.chat.id, "<b>Оберіть літеру вашого класу</b>", parse_mode="html", reply_markup=class_num())

    @bot.message_handler(commands=["А"])
    def A_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Б"])
    def B_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["В"])
    def C_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Г"])
    def G_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Текст"])
    def text_message(message):
        bot.send_message(message.chat.id, scheule_11C, parse_mode="html")
        time.sleep(1)
        bot.send_message(message.chat.id, "<b>Оберіть функцію з поданих нижче</b>", reply_markup=start_button_func(),parse_mode="HTML")
    pass

    @bot.message_handler(commands=["Фото"])
    def photo(message):
        with open("/Users/stasuk2007/Documents/istockphoto-525430193-612x612.jpg", "rb") as file:
            bot.send_photo(message.chat.id, file)
            time.sleep(1)
            bot.send_message(message.chat.id, "<b>Оберіть функцію з поданих нижче</b>",reply_markup=start_button_func(), parse_mode="HTML")
        pass
    pass

@bot.message_handler(commands=["6_класи"])
def sixth(message):
    bot.send_message(message.chat.id, "<b>Оберіть літеру вашого класу</b>", parse_mode="html", reply_markup=class_num())

    @bot.message_handler(commands=["А"])
    def A_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Б"])
    def B_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["В"])
    def C_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Г"])
    def G_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Текст"])
    def text_message(message):
        bot.send_message(message.chat.id, scheule_11C, parse_mode="html")
        time.sleep(1)
        bot.send_message(message.chat.id, "<b>Оберіть функцію з поданих нижче</b>", reply_markup=start_button_func(), parse_mode="HTML")
    pass

    @bot.message_handler(commands=["Фото"])
    def photo(message):
        with open("/Users/stasuk2007/Documents/istockphoto-525430193-612x612.jpg", "rb") as file:
            bot.send_photo(message.chat.id, file)
            time.sleep(1)
            bot.send_message(message.chat.id, "<b>Оберіть функцію з поданих нижче</b>",reply_markup=start_button_func(), parse_mode="HTML")
        pass
    pass

@bot.message_handler(commands=["5_класи"])
def fifth(message):
    bot.send_message(message.chat.id, "<b>Оберіть літеру вашого класу</b>", parse_mode="html", reply_markup=class_num())

    @bot.message_handler(commands=["А"])
    def A_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Б"])
    def B_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["В"])
    def C_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Г"])
    def G_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>",reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Текст"])
    def text_message(message):
        bot.send_message(message.chat.id, scheule_11C, parse_mode="html")
        time.sleep(1)
        bot.send_message(message.chat.id, "<b>Оберіть функцію з поданих нижче</b>", reply_markup=start_button_func(),parse_mode="HTML")
    pass

    @bot.message_handler(commands=["Фото"])
    def photo(message):
        with open("/Users/stasuk2007/Documents/image1.png", "rb") as file:
            bot.send_photo(message.chat.id, file)
            time.sleep(1)
            bot.send_message(message.chat.id, "<b>Оберіть функцію з поданих нижче</b>",reply_markup=start_button_func(), parse_mode="HTML")
        pass
    pass


bot.polling(non_stop=True)