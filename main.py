import time

import telebot as tb
import webbrowser

from Buttons import start_button_func, schedule_buttons
from Buttons import class_num
from Schedule import scheule_11C
from Buttons import des
from Buttons import notes_button


API_TOKEN = '7417043537:AAE2iriywyeavMpluQ2iPNPjAAigVJxoYr0'
bot = tb.TeleBot(API_TOKEN)



@bot.message_handler(commands=['Сайт'])
def site(message):
    webbrowser.open("https://www.reddit.com")


@bot.message_handler(commands=["start"])
def start_function(message):
    bot.send_message(message.chat.id, "<b>Всіх вітаю!Це офіційний телеграм бот 5 школи.</b>", parse_mode="html",reply_markup=start_button_func())

@bot.message_handler(commands=["Додаток"])
def app(message):
    bot.reply_to(message, "<b>Це платформа на якій ви можете детальніше дізнатись про розклад уроків.Натисніть на <u>/App</u> щоб відкрити</b>", parse_mode="html")

@bot.message_handler(commands=["App"])
def app(message):
    webbrowser.open("https://apps.apple.com/ua/app/%D1%94%D0%B4%D0%B8%D0%BD%D0%B0-%D1%88%D0%BA%D0%BE%D0%BB%D0%B0/id1447875950?l=uk")

@bot.message_handler(commands=["Нотатки"])
def notes(message):
    bot.send_message(message.chat.id, "<b>Оберіть одну з поданих функцій</b>" ,parse_mode="html",reply_markup=notes_button())


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
        with open("/Users/stasuk2007/Documents/istockphoto-525430193-612x612.jpg", "rb") as file:
            bot.send_photo(message.chat.id, file)
            time.sleep(1)
            bot.send_message(message.chat.id, "<b>Оберіть функцію з поданих нижче</b>",reply_markup=start_button_func(), parse_mode="HTML")
        pass
    pass


bot.polling(non_stop=True)