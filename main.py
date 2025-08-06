import time
from math import lgamma

import telebot as tb

from datetime import datetime
from Notes import  notes_save
from Notes import  notes_data
from Buttons import start_button_func, schedule_buttons, notes_button
from Buttons import class_num
from Schedule import scheule_11C, schedule_11A, schedule_11B, schedule_11G, schedule_10A, schedule_10B, schedule_10C, schedule_10G, schedule_9A, schedule_9B, schedule_5C, schedule_5A, schedule_6A, schedule_7A,schedule_5B, schedule_6C, schedule_5G ,schedule_8A, schedule_6B, schedule_7B,schedule_8B, schedule_7C, schedule_6G, schedule_7G, schedule_8C, schedule_9C, schedule_8G, schedule_9G
from Buttons import des
from Buttons import site_buttons
from Buttons import app_buttons


API_TOKEN = ''
bot = tb.TeleBot(API_TOKEN)

url = "https://www.reddit.com"


@bot.message_handler(commands=["start"])
def start_function(message):
    bot.send_message(message.chat.id, "<b>Всіх вітаю!Це офіційний телеграм бот ліцею 5 в Ужгороді.</b>", parse_mode="html",reply_markup=start_button_func())

@bot.message_handler(func=lambda message: message.text in ["Повернутись на початок"])
def quit(message):
    bot.send_message(message.chat.id, "<b>Ви повернулись на початок</b>", parse_mode="html", reply_markup=start_button_func())

@bot.message_handler(func=lambda message: message.text in ["Додаток"])
def app (message):
    bot.send_message(message.chat.id, "<b>Ось наш додаток.Виберіть ОС якою ви користуєтесь задля подальшого відвідання додатку</b>", parse_mode="html", reply_markup = app_buttons())


@bot.message_handler(func=lambda message: message.text in ["Наш сайт"])
def app(message):
    bot.send_message(message.chat.id,"<b>Це наш сайт</b>",parse_mode="html", reply_markup=site_buttons())


@bot.message_handler(func=lambda message: message.text in ["Повернутись на початок"])
def notes(message):
    bot.send_message(message.chat.id, "<b>Виберіть одну з поданих функцій</b>", parse_mode="html", reply_markup=start_button_func())

@bot.message_handler(func=lambda message: message.text in ["Нотатки"])
def notes(message):
        chat_id = str(message.chat.id)
        user_notes = notes_data.get(chat_id, [])

        if isinstance(user_notes, list):
            notes_text = "\n".join(f"{i + 1}. {note.get('text', 'Невідома нотатка')} (📅 {note.get('date', 'Невідома дата')})" for i, note in enumerate(user_notes) if isinstance(note, dict))
            bot.send_message(chat_id, f"f<b>Ваші нотатки</b>\n{notes_text}" if notes_text else "<b>У вас ще немає нотаток</b>", parse_mode="html" ,reply_markup=notes_button())
        else:
            bot.send_message(chat_id, "<b>Помилка формату нотаток</b>", parse_mode="html", reply_markup=notes_button())


@bot.message_handler(func=lambda message: message.text in ["Створити"])
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

@bot.message_handler(func=lambda message: message.text in ["Очистити"])
def clear_notes(message):
        chat_id = str(message.chat.id)
        if chat_id in notes_data:
            del notes_data[chat_id]
            notes_save(notes_data)
            bot.send_message(chat_id, "🗑️<b>Немає нотаток,оскільки всі нотатки видалені</b>",parse_mode="html", reply_markup=notes_button())
        else:
            bot.send_message(chat_id, "❗<b>У️ вас немає нотаток для видалення</b>", parse_mode="html")
        pass


@bot.message_handler(func=lambda message: message.text in ["Подивитись"])
def view_notes(message):
        chat_id = str(message.chat.id)
        user_notes = notes_data.get(chat_id, [])


        if isinstance(user_notes, list):
            notes_text = "\n".join(f"{i + 1}. {note.get('text', 'Невідома нотатка')} (📅 {note.get('date', 'Невідома дата')})" for i, note in enumerate(user_notes) if isinstance(note, dict))
            bot.send_message(chat_id, f"<b>Ваші нотатки:</b>\n{notes_text}" if notes_text else "<b>У вас ще немає нотаток.</b>",parse_mode="html")
        else:
            bot.send_message(chat_id,"<b>‽Помилка в форматі нотаток</b>",reply_markup=notes_button(), parse_mode="html")
        return view_notes

@bot.message_handler(func=lambda message: message.text == "Вийти")
def quite(message):
        bot.send_message(message.chat.id, "<b>Виберіть одну з поданих функцій</b>", reply_markup=start_button_func(), parse_mode="html")


@bot.message_handler(func=lambda message: message.text in ["Домашня робота"])
def homework(message):
    bot.send_message(message.chat.id, "<b>Ось ваше домашнє завдання</b>", parse_mode="html")


@bot.message_handler(func=lambda message: message.text in ["Розклад уроків"])
def schedule(message):
    bot.send_message(message.chat.id,"<b>Оберіть ваш клас з поданих нижче,щоб отримати свій розклад</b>",parse_mode="html",reply_markup=schedule_buttons())


user_states11 = {}


@bot.message_handler(func=lambda message: message.text == "11 клас")
def choose_class_letter(message):
    chat_id = message.chat.id
    user_states11[chat_id] = {"grade": "11"}
    bot.send_message(chat_id, "<b>Оберіть літеру вашого класу</b>", parse_mode="html", reply_markup=class_num())


@bot.message_handler(func=lambda message: message.text in ["А", "Б", "В", "Г"])
def select_class_letter(message):
    chat_id = message.chat.id
    if chat_id in user_states11 and user_states11[chat_id].get("grade") == "11":
        selected_letter = message.text
        user_states11[chat_id]["letter"] = selected_letter
        bot.send_message(chat_id,f"<b>Ви обрали літеру {selected_letter}. Тепер оберіть варіант в якому ви хочете отримати розклад:</b>", parse_mode="html", reply_markup=des())


@bot.message_handler(func=lambda message: message.text in ["Текстовий варіант", "Зображення"])
def send_schedule(message):
    chat_id = message.chat.id
    user_info = user_states11.get(chat_id)

    if not user_info or user_info.get("grade") != "11":
        bot.send_message(chat_id, "<b>Спочатку оберіть клас</b>", parse_mode="html")
        return

    letter = user_info.get("letter")

    if message.text == "Текстовий варіант":
        schedules = {
            "А": schedule_11A,
            "Б": schedule_11B,
            "В": scheule_11C,
            "Г": schedule_11G,
        }
        schedule_text = schedules.get(letter)
        if schedule_text:
            bot.send_message(chat_id, schedule_text, parse_mode="html")
        else:
            bot.send_message(chat_id, "Немає поданого класу в базі даних", parse_mode="html")

    elif message.text == "Зображення":
        photos = {
            "А": "Schedule_photo/Знімок екрана 2025-05-13 о 22.13.22.png",
            "Б": "Schedule_photo/Знімок екрана 2025-05-03 о 20.02.24.png",
            "В": "Schedule_photo/Screenshot 2025-03-22 at 21.44.24.png",
            "Г": "Schedule_photo/Screenshot 2025-03-24 at 11.09.31.png",
        }
        photo_path = photos.get(letter)
        if photo_path:
            with open(photo_path, "rb") as file:
                bot.send_photo(chat_id, file)
        else:
            bot.send_message(chat_id, "Немає поданого класу в базі даних", parse_mode="html")


    time.sleep(1)
    bot.send_message(chat_id, "<b>Оберіть функцію з поданих нижче</b>", reply_markup=start_button_func(), parse_mode="html")

user_states10 ={}

@bot.message_handler(func=lambda message: message.text == "10 клас")
def choose_class_letter(message):
    chat_id = message.chat.id
    user_states10[chat_id] = {"grade": "10"}
    bot.send_message(chat_id, "<b>Оберіть літеру вашого класу</b>", parse_mode="html", reply_markup=class_num())


@bot.message_handler(func=lambda message: message.text in ["А", "Б", "В", "Г"])
def select_class_letter(message):
    chat_id = message.chat.id
    if chat_id in user_states10 and user_states10[chat_id].get("grade") == "10":
        selected_letter = message.text
        user_states10[chat_id]["letter"] = selected_letter
        bot.send_message(chat_id,f"<b>Ви обрали літеру {selected_letter}. Тепер оберіть варіант в якому ви хочете отримати розклад:</b>", parse_mode="html", reply_markup=des())


@bot.message_handler(func=lambda message: message.text in ["Текстовий варіант", "Зображення"])
def send_schedule(message):
    chat_id = message.chat.id
    user_info = user_states10.get(chat_id)

    if not user_info or user_info.get("grade") != "10":
        bot.send_message(chat_id, "<b>Спочатку оберіть клас</b>", parse_mode="html")
        return

    letter = user_info.get("letter")

    if message.text == "Текстовий варіант":
        schedules = {
            "А": schedule_10A,
            "Б": schedule_10B,
            "В": schedule_10C,
            "Г": schedule_10G,
        }
        schedule_text = schedules.get(letter)
        if schedule_text:
            bot.send_message(chat_id, schedule_text, parse_mode="html")
        else:
            bot.send_message(chat_id, "Немає поданого класу в базі даних", parse_mode="html")

    elif message.text == "Зображення":
        photos = {
            "А": "Schedule_photo/Знімок екрана 2025-05-13 о 22.13.22.png",
            "Б": "Schedule_photo/Знімок екрана 2025-05-03 о 20.02.24.png",
            "В": "Schedule_photo/Screenshot 2025-03-22 at 21.44.24.png",
            "Г": "Schedule_photo/Screenshot 2025-03-24 at 11.09.31.png",
        }
        photo_path = photos.get(letter)
        if photo_path:
            with open(photo_path, "rb") as file:
                bot.send_photo(chat_id, file)
        else:
            bot.send_message(chat_id, "Немає поданого класу в базі даних", parse_mode="html")


    time.sleep(1)
    bot.send_message(chat_id, "<b>Оберіть функцію з поданих нижче</b>", reply_markup=start_button_func(), parse_mode="html")


user_states9 = {}

@bot.message_handler(func=lambda message: message.text == "9 клас")
def choose_class_letter(message):
    chat_id = message.chat.id
    user_states9[chat_id] = {"grade": "9"}
    bot.send_message(chat_id, "<b>Оберіть літеру вашого класу</b>", parse_mode="html", reply_markup=class_num())


@bot.message_handler(func=lambda message: message.text in ["А", "Б", "В", "Г"])
def select_class_letter(message):
    chat_id = message.chat.id
    if chat_id in user_states9 and user_states9[chat_id].get("grade") == "9":
        selected_letter = message.text
        user_states9[chat_id]["letter"] = selected_letter
        bot.send_message(chat_id,f"<b>Ви обрали літеру {selected_letter}. Тепер оберіть варіант в якому ви хочете отримати розклад:</b>", parse_mode="html", reply_markup=des())


@bot.message_handler(func=lambda message: message.text in ["Текстовий варіант", "Зображення"])
def send_schedule(message):
    chat_id = message.chat.id
    user_info = user_states9.get(chat_id)

    if not user_info or user_info.get("grade") != "9":
        bot.send_message(chat_id, "<b>Спочатку оберіть клас</b>", parse_mode="html")
        return

    letter = user_info.get("letter")

    if message.text == "Текстовий варіант":
        schedules = {
            "А": schedule_9A,
            "Б": schedule_9B,
            "В": schedule_9C,
            "Г": schedule_9G,
        }
        schedule_text = schedules.get(letter)
        if schedule_text:
            bot.send_message(chat_id, schedule_text, parse_mode="html")
        else:
            bot.send_message(chat_id, "Немає поданого класу в базі даних", parse_mode="html")

    elif message.text == "Зображення":
        photos = {
            "А": "Schedule_photo/Знімок екрана 2025-05-13 о 22.13.22.png",
            "Б": "Schedule_photo/Знімок екрана 2025-05-03 о 20.02.24.png",
            "В": "Schedule_photo/Screenshot 2025-03-22 at 21.44.24.png",
            "Г": "Schedule_photo/Screenshot 2025-03-24 at 11.09.31.png",
        }
        photo_path = photos.get(letter)
        if photo_path:
            with open(photo_path, "rb") as file:
                bot.send_photo(chat_id, file)
        else:
            bot.send_message(chat_id, "Немає поданого класу в базі даних", parse_mode="html")


    time.sleep(1)
    bot.send_message(chat_id, "<b>Оберіть функцію з поданих нижче</b>", reply_markup=start_button_func(), parse_mode="html")

user_states8 = {}

@bot.message_handler(func=lambda message: message.text == "8 клас")
def choose_class_letter(message):
    chat_id = message.chat.id
    user_states8[chat_id] = {"grade": "8"}
    bot.send_message(chat_id, "<b>Оберіть літеру вашого класу</b>", parse_mode="html", reply_markup=class_num())


@bot.message_handler(func=lambda message: message.text in ["А", "Б", "В", "Г"])
def select_class_letter(message):
    chat_id = message.chat.id
    if chat_id in user_states8 and user_states8[chat_id].get("grade") == "8":
        selected_letter = message.text
        user_states8[chat_id]["letter"] = selected_letter
        bot.send_message(chat_id,f"<b>Ви обрали літеру {selected_letter}. Тепер оберіть варіант в якому ви хочете отримати розклад:</b>", parse_mode="html", reply_markup=des())


@bot.message_handler(func=lambda message: message.text in ["Текстовий варіант", "Зображення"])
def send_schedule(message):
    chat_id = message.chat.id
    user_info = user_states8.get(chat_id)

    if not user_info or user_info.get("grade") != "8":
        bot.send_message(chat_id, "<b>Спочатку оберіть клас</b>", parse_mode="html")
        return

    letter = user_info.get("letter")

    if message.text == "Текстовий варіант":
        schedules = {
            "А": schedule_8A,
            "Б": schedule_8B,
            "В": schedule_8C,
            "Г": schedule_8G,
        }
        schedule_text = schedules.get(letter)
        if schedule_text:
            bot.send_message(chat_id, schedule_text, parse_mode="html")
        else:
            bot.send_message(chat_id, "Немає поданого класу в базі даних", parse_mode="html")

    elif message.text == "Зображення":
        photos = {
            "А": "Schedule_photo/Знімок екрана 2025-05-13 о 22.13.22.png",
            "Б": "Schedule_photo/Знімок екрана 2025-05-03 о 20.02.24.png",
            "В": "Schedule_photo/Screenshot 2025-03-22 at 21.44.24.png",
            "Г": "Schedule_photo/Screenshot 2025-03-24 at 11.09.31.png",
        }
        photo_path = photos.get(letter)
        if photo_path:
            with open(photo_path, "rb") as file:
                bot.send_photo(chat_id, file)
        else:
            bot.send_message(chat_id, "Немає поданого класу в базі даних", parse_mode="html")


    time.sleep(1)
    bot.send_message(chat_id, "<b>Оберіть функцію з поданих нижче</b>", reply_markup=start_button_func(), parse_mode="html")

user_states7 = {}

@bot.message_handler(func=lambda message: message.text == "7 клас")
def choose_class_letter(message):
    chat_id = message.chat.id
    user_states7[chat_id] = {"grade": "7"}
    bot.send_message(chat_id, "<b>Оберіть літеру вашого класу</b>", parse_mode="html", reply_markup=class_num())


@bot.message_handler(func=lambda message: message.text in ["А", "Б", "В", "Г"])
def select_class_letter(message):
    chat_id = message.chat.id
    if chat_id in user_states7 and user_states7[chat_id].get("grade") == "11":
        selected_letter = message.text
        user_states7[chat_id]["letter"] = selected_letter
        bot.send_message(chat_id,f"<b>Ви обрали літеру {selected_letter}. Тепер оберіть варіант в якому ви хочете отримати розклад:</b>", parse_mode="html", reply_markup=des())


@bot.message_handler(func=lambda message: message.text in ["Текстовий варіант", "Зображення"])
def send_schedule(message):
    chat_id = message.chat.id
    user_info = user_states7.get(chat_id)

    if not user_info or user_info.get("grade") != "11":
        bot.send_message(chat_id, "<b>Спочатку оберіть клас</b>", parse_mode="html")
        return

    letter = user_info.get("letter")

    if message.text == "Текстовий варіант":
        schedules = {
            "А": schedule_7A,
            "Б": schedule_7B,
            "В": schedule_7C,
            "Г": schedule_7G,
        }
        schedule_text = schedules.get(letter)
        if schedule_text:
            bot.send_message(chat_id, schedule_text, parse_mode="html")
        else:
            bot.send_message(chat_id, "Немає поданого класу в базі даних", parse_mode="html")

    elif message.text == "Зображення":
        photos = {
            "А": "Schedule_photo/Знімок екрана 2025-05-13 о 22.13.22.png",
            "Б": "Schedule_photo/Знімок екрана 2025-05-03 о 20.02.24.png",
            "В": "Schedule_photo/Screenshot 2025-03-22 at 21.44.24.png",
            "Г": "Schedule_photo/Screenshot 2025-03-24 at 11.09.31.png",
        }
        photo_path = photos.get(letter)
        if photo_path:
            with open(photo_path, "rb") as file:
                bot.send_photo(chat_id, file)
        else:
            bot.send_message(chat_id, "Немає поданого класу в базі даних", parse_mode="html")


    time.sleep(1)
    bot.send_message(chat_id, "<b>Оберіть функцію з поданих нижче</b>", reply_markup=start_button_func(), parse_mode="html")

user_states6 = {}

@bot.message_handler(func=lambda message: message.text == "6 клас")
def choose_class_letter(message):
    chat_id = message.chat.id
    user_states6[chat_id] = {"grade": "6"}
    bot.send_message(chat_id, "<b>Оберіть літеру вашого класу</b>", parse_mode="html", reply_markup=class_num())


@bot.message_handler(func=lambda message: message.text in ["А", "Б", "В", "Г"])
def select_class_letter(message):
    chat_id = message.chat.id
    if chat_id in user_states6 and user_states6[chat_id].get("grade") == "6":
        selected_letter = message.text
        user_states6[chat_id]["letter"] = selected_letter
        bot.send_message(chat_id,f"<b>Ви обрали літеру {selected_letter}. Тепер оберіть варіант в якому ви хочете отримати розклад:</b>", parse_mode="html", reply_markup=des())


@bot.message_handler(func=lambda message: message.text in ["Текстовий варіант", "Зображення"])
def send_schedule(message):
    chat_id = message.chat.id
    user_info = user_states6.get(chat_id)

    if not user_info or user_info.get("grade") != "6":
        bot.send_message(chat_id, "<b>Спочатку оберіть клас</b>", parse_mode="html")
        return

    letter = user_info.get("letter")

    if message.text == "Текстовий варіант":
        schedules = {
            "А": schedule_6A,
            "Б": schedule_6B,
            "В": schedule_6C,
            "Г": schedule_6G,
        }
        schedule_text = schedules.get(letter)
        if schedule_text:
            bot.send_message(chat_id, schedule_text, parse_mode="html")
        else:
            bot.send_message(chat_id, "Немає поданого класу в базі даних", parse_mode="html")

    elif message.text == "Зображення":
        photos = {
            "А": "Schedule_photo/Знімок екрана 2025-05-13 о 22.13.22.png",
            "Б": "Schedule_photo/Знімок екрана 2025-05-03 о 20.02.24.png",
            "В": "Schedule_photo/Screenshot 2025-03-22 at 21.44.24.png",
            "Г": "Schedule_photo/Screenshot 2025-03-24 at 11.09.31.png",
        }
        photo_path = photos.get(letter)
        if photo_path:
            with open(photo_path, "rb") as file:
                bot.send_photo(chat_id, file)
        else:
            bot.send_message(chat_id, "Немає поданого класу в базі даних", parse_mode="html")


    time.sleep(1)
    bot.send_message(chat_id, "<b>Оберіть функцію з поданих нижче</b>", reply_markup=start_button_func(), parse_mode="html")

user_states5 = {}

@bot.message_handler(func=lambda message: message.text == "5 клас")
def choose_class_letter(message):
    chat_id = message.chat.id
    user_states5[chat_id] = {"grade": "5"}
    bot.send_message(chat_id, "<b>Оберіть літеру вашого класу</b>", parse_mode="html", reply_markup=class_num())


@bot.message_handler(func=lambda message: message.text in ["А", "Б", "В", "Г"])
def select_class_letter(message):
    chat_id = message.chat.id
    if chat_id in user_states5 and user_states5[chat_id].get("grade") == "5":
        selected_letter = message.text
        user_states5[chat_id]["letter"] = selected_letter
        bot.send_message(chat_id,f"<b>Ви обрали літеру {selected_letter}. Тепер оберіть варіант в якому ви хочете отримати розклад:</b>", parse_mode="html", reply_markup=des())


@bot.message_handler(func=lambda message: message.text in ["Текстовий варіант", "Зображення"])
def send_schedule(message):
    chat_id = message.chat.id
    user_info = user_states5.get(chat_id)

    if not user_info or user_info.get("grade") != "5":
        bot.send_message(chat_id, "<b>Спочатку оберіть клас</b>", parse_mode="html")
        return

    letter = user_info.get("letter")

    if message.text == "Текстовий варіант":
        schedules = {
            "А": schedule_5A,
            "Б": schedule_5B,
            "В": schedule_5C,
            "Г": schedule_5G,
        }
        schedule_text = schedules.get(letter)
        if schedule_text:
            bot.send_message(chat_id, schedule_text, parse_mode="html")
        else:
            bot.send_message(chat_id, "Немає поданого класу в базі даних", parse_mode="html")

    elif message.text == "Зображення":
        photos = {
            "А": "Schedule_photo/Знімок екрана 2025-05-13 о 22.13.22.png",
            "Б": "Schedule_photo/Знімок екрана 2025-05-03 о 20.02.24.png",
            "В": "Schedule_photo/Screenshot 2025-03-22 at 21.44.24.png",
            "Г": "Schedule_photo/Screenshot 2025-03-24 at 11.09.31.png",
        }
        photo_path = photos.get(letter)
        if photo_path:
            with open(photo_path, "rb") as file:
                bot.send_photo(chat_id, file)
        else:
            bot.send_message(chat_id, "Немає поданого класу в базі даних", parse_mode="html")


    time.sleep(1)
    bot.send_message(chat_id, "<b>Оберіть функцію з поданих нижче</b>", reply_markup=start_button_func(), parse_mode="html")


bot.polling(non_stop=True)
