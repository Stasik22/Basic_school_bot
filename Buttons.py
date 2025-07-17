from telebot.types import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup
def start_button_func():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    Schedule = InlineKeyboardButton("Розклад уроків")
    notes = InlineKeyboardButton("Нотатки")
    site = InlineKeyboardButton("Наш сайт")
    app = InlineKeyboardButton("Додаток")
    homework = InlineKeyboardButton("Домашня робота")
    keyboard.add(Schedule, notes, site, app, homework)
    return keyboard


def schedule_buttons():
    schedule_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4, one_time_keyboard=True)
    eleventh_classes = InlineKeyboardButton("11 клас")
    tenth_classes = InlineKeyboardButton("10 клас")
    ninth_classes = InlineKeyboardButton("9 клас")
    eighth_classes = InlineKeyboardButton("8 клас")
    seventh_classes = InlineKeyboardButton("7 клас")
    sixth_classes = InlineKeyboardButton("6 клас")
    fifth_classes = InlineKeyboardButton("5 клас")
    schedule_keyboard.add(eleventh_classes, tenth_classes, ninth_classes, eighth_classes, seventh_classes , sixth_classes, fifth_classes)
    return schedule_keyboard


def des():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    text = InlineKeyboardButton("Текстовий варіант")
    photo = InlineKeyboardButton("Зображення")
    Quit = InlineKeyboardButton("Повернутись на початок")
    keyboard.add(text, photo, Quit)
    return keyboard

def class_num():
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2)
    A = InlineKeyboardButton("А")
    B = InlineKeyboardButton("Б")
    V = InlineKeyboardButton("В")
    G = InlineKeyboardButton("Г")
    Quit = InlineKeyboardButton("Повернутись на початок")
    keyboard.add(A, B, V, G, Quit)
    return keyboard


def notes_button():
    keyboard = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
    create = InlineKeyboardButton("Створити")
    deletee = InlineKeyboardButton("Очистити")
    show = InlineKeyboardButton("Подивитись")
    quit = InlineKeyboardButton("Вийти")
    keyboard.add(create, deletee, show, quit)
    return keyboard


def site_buttons():
    markup = InlineKeyboardMarkup()
    keyboard = InlineKeyboardButton("Відкрити сайт", url = "https://www.twitch.tv/")
    markup.add(keyboard)
    return markup



def app_buttons():
    IOS_url = "https://apps.apple.com/ua/app/%D1%94%D0%B4%D0%B8%D0%BD%D0%B0-%D1%88%D0%BA%D0%BE%D0%BB%D0%B0/id1447875950?l=ru"
    Android_url = "https://play.google.com/store/apps/details?id=com.tatl.technology.usu_fp_schedule"
    markup = InlineKeyboardMarkup()
    keyboard = InlineKeyboardButton("IOS", url= IOS_url)
    keyboard_x2 = InlineKeyboardButton("Android", url = Android_url)
    markup.add(keyboard, keyboard_x2)
    return markup