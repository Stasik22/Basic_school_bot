import time
import json
import telebot as tb



from Buttons import start_button_func, schedule_buttons
from Buttons import class_num
from Schedule import scheule_11C
from Buttons import des
from Buttons import site_buttons
from Buttons import app_buttons

API_TOKEN = '7417043537:AAE2iriywyeavMpluQ2iPNPjAAigVJxoYr0'
bot = tb.TeleBot(API_TOKEN)

NOTES_FILE = "notes.json"

def notes_load():
    try:
        with open(NOTES_FILE, "r", encoding= "utf-8") as file:
            return json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        return {}

def notes_save(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as file:
        json.dump(file, notes, indent=4, ensure_ascii=False)

notes_data = notes_load()

@bot.message_handler(commands=["Нотатки"])
def notes(message):
    chat_id = str(message.chat.id)
    user_notes = notes_data.get(chat_id, [])

    if isinstance(user_notes, list):
        notes_text = "\n".join(f"{i + 1}.{note.get('text', 'yt')}")


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
    bot.send_message(message.chat.id,"<b>Оберіть літеру вашого класу</b>", parse_mode="html", reply_markup=class_num())
    @bot.message_handler(commands=["А"])
    def A_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>", reply_markup=des(), parse_mode="html")
    pass

    @bot.message_handler(commands=["Б"])
    def B_class(message):
        bot.send_message(message.chat.id, "<b>Виберіть варіант в якому ви хочете отримати повідомлення</b>", reply_markup=des(), parse_mode="html")
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


@bot.message_handler(commands=["10_класи"])
def tenth(message):
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