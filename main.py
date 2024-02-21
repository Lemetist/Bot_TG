import telebot
from telebot import types

# Здесь указываем токен вашего бота
TOKEN = ''

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)

# Список фамилий отсутствующих
absentees = [
    "Алаторцев П.В.",
    "Багиров Э.Э.",
    "Башкиров И.В.",
    "Борхоев Б.Б.",
    "Евстафьев А.А.",
    "Журавлева М.Р.",
    "Киреев А.А.",
    "Ламажап Н.А.",
    "Ленючев Д.А.",
    "Львов М.Д.",
    "Макаров Е.С.",
    "Овчинникова И.А.",
    "Подлинный М.В.",
    "Сатин Т.С.",
    "Секункова П.А.",
    "Семечаевский П.В.",
    "Сержантов И.А.",
    "Токарев А.Д.",
    "Чичёв А.Б.",
    "Шахкиримов К.И.",
    "Шишалов С.Д.",
    "Максимов М.М.",
    "Маковский А.С."
]

# Создаем клавиатуру для выбора отсутствующих
def generate_keyboard():
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for name in absentees:
        button = types.KeyboardButton(name)
        keyboard.add(button)
    return keyboard

# Команда /start для начала общения с ботом
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Посмотреть список')
    itembtn2 = types.KeyboardButton('Заполнить список заново')
    itembtn3 = types.KeyboardButton('Выбрать присутствующих')
    markup.add(itembtn1, itembtn2, itembtn3)

    if len(absentees) > 0:
        bot.send_message(message.chat.id,
                         "Привет! Я твой бот для учета отсутствующих. Чтобы выбрать действие, нажми на соответствующую кнопку.",
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id,
                         "Привет! Я твой бот для учета отсутствующих. На данный момент отсутствующих нет.",
                         reply_markup=markup)


# Команда /absentees для вывода списка отсутствующих
@bot.message_handler(commands=['absentees'])
def show_absentees(message):
    if len(absentees) > 0:
        bot.send_message(message.chat.id, "Список отсутствующих:\n" + "\n".join(absentees))
    else:
        bot.send_message(message.chat.id, "На данный момент отсутствующих нет.")

# Команда /fill для заполнения списка заново
@bot.message_handler(commands=['fill'])
def refill_absentees(message):
    global absentees

    absentees = [
    "Алаторцев П.В.",
    "Багиров Э.Э.",
    "Башкиров И.В.",
    "Борхоев Б.Б.",
    "Евстафьев А.А.",
    "Журавлева М.Р.",
    "Киреев А.А.",
    "Ламажап Н.А.",
    "Ленючев Д.А.",
    "Львов М.Д.",
    "Макаров Е.С.",
    "Овчинникова И.А.",
    "Подлинный М.В.",
    "Сатин Т.С.",
    "Секункова П.А.",
    "Семечаевский П.В.",
    "Сержантов И.А.",
    "Токарев А.Д.",
    "Чичёв А.Б.",
    "Шахкиримов К.И.",
    "Шишалов С.Д.",
    "Максимов М.М.",
    "Маковский А.С."
]
    bot.send_message(message.chat.id, "Список отсутствующих успешно заполнен заново.")

# Обработчик нажатий на кнопки
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == 'Посмотреть список':
        show_absentees(message)
    elif message.text == 'Заполнить список заново':
        refill_absentees(message)
    elif message.text == 'Выбрать присутствующих':
        bot.send_message(message.chat.id, "Выбрать присутствующих:", reply_markup=generate_keyboard())
    elif message.text in absentees:
        remove_absentee(message)
    else:
        bot.send_message(message.chat.id, "Неизвестная команда. Используйте кнопки для взаимодействия.")

# Обработчик выбора отсутствующего
def remove_absentee(message):
    global absentees
    removed_name = message.text
    absentees.remove(removed_name)
    bot.send_message(message.chat.id, f"{removed_name} удален из списка отсутствующих.")
    bot.send_message(message.chat.id, "Выбрать присутствующих:", reply_markup=generate_keyboard())

# Запускаем бота
bot.polling()
