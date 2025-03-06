from telebot.types import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup

def start_button_func():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    Schedule = InlineKeyboardButton("/Розклад")
    notes = InlineKeyboardButton("/Нотатки")
    site = InlineKeyboardButton("/Сайт")
    app = InlineKeyboardButton("/Додаток")
    homework = InlineKeyboardButton("/Домашня")
    keyboard.add(Schedule, notes, site, app, homework)
    return keyboard
pass

def schedule_buttons():
    schedule_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4, one_time_keyboard=True)
    eleventh_classes = InlineKeyboardButton("/11_класи")
    tenth_classes = InlineKeyboardButton("/10_класи")
    ninth_classes = InlineKeyboardButton("/9_класи")
    eighth_classes = InlineKeyboardButton("/8_класи")
    seventh_classes = InlineKeyboardButton("/7_класи")
    sixth_classes = InlineKeyboardButton("/6_класи")
    fifth_classes = InlineKeyboardButton("/5_класи")
    schedule_keyboard.add(eleventh_classes, tenth_classes, ninth_classes, eighth_classes, seventh_classes , sixth_classes, fifth_classes)
    return schedule_keyboard
pass

def des():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    text = InlineKeyboardButton("/Текст")
    photo = InlineKeyboardButton("/Фото")
    keyboard.add(text, photo)
    return keyboard
pass

def class_num():
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2)
    A = InlineKeyboardButton("/А")
    B = InlineKeyboardButton("/Б")
    V = InlineKeyboardButton("/В")
    G = InlineKeyboardButton("/Г")
    keyboard.add(A, B, V, G)
    return keyboard
pass

def notes_button():
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)
    create = InlineKeyboardButton("/Створити")
    deletee = InlineKeyboardButton("/Очистити")
    show = InlineKeyboardButton("/Переглянути")
    keyboard.add(create, deletee, show)
    return keyboard
pass

def site_buttons():
    url = "https://www.reddit.com"
    markup = InlineKeyboardMarkup()
    keyboard = InlineKeyboardButton("Відкрити сайт", url = url)
    markup.add(keyboard)
    return markup
pass


def app_buttons():
    IOS_url = "https://apps.apple.com/ua/app/%D1%94%D0%B4%D0%B8%D0%BD%D0%B0-%D1%88%D0%BA%D0%BE%D0%BB%D0%B0/id1447875950?l=ru"
    Android_url = "https://play.google.com/store/apps/details?id=com.tatl.technology.usu_fp_schedule"
    markup = InlineKeyboardMarkup()
    keyboard = InlineKeyboardButton("Відкрити додаток на IOS", url = IOS_url)
    keyboard_x2 = InlineKeyboardButton("Відкрити додаток на Android", url = Android_url)
    markup.add(keyboard, keyboard_x2)
    return markup
pass









