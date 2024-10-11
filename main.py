import telebot
from telebot import types
from datetime import date
from config import TOKEN

class AbsenteeBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.absentees = [
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
        self.setup_handlers()

    def generate_keyboard(self):
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        for name in self.absentees:
            button = types.KeyboardButton(name)
            keyboard.add(button)
        keyboard.add(types.KeyboardButton('Вернуться на /start'))
        return keyboard

    def start(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Посмотреть список')
        itembtn2 = types.KeyboardButton('Заполнить список заново')
        itembtn3 = types.KeyboardButton('Выбрать присутствующих')
        markup.add(itembtn1, itembtn2, itembtn3)

        if len(self.absentees) > 0:
            self.bot.send_message(message.chat.id,
                             "Привет! Я твой бот для учета отсутствующих. Чтобы выбрать действие, нажми на соответствующую кнопку.",
                             reply_markup=markup)
        else:
            self.bot.send_message(message.chat.id,
                             "Привет! Я твой бот для учета отсутствующих. На данный момент отсутствующих нет.",
                             reply_markup=markup)

    def show_absentees(self, message):
        if len(self.absentees) > 0:
            self.bot.send_message(message.chat.id, f"{date.today()}")
            absentees_list = "\n".join(self.absentees)
            self.bot.send_message(message.chat.id, f"Список отсутствующих:\n{absentees_list}")
        else:
            self.bot.send_message(message.chat.id, "На данный момент отсутствующих нет.")

    def refill_absentees(self, message):
        self.absentees = [
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
        self.bot.send_message(message.chat.id, "Список отсутствующих успешно заполнен заново.")

    def handle_buttons(self, message):
        if message.text == 'Посмотреть список':
            self.show_absentees(message)
        elif message.text == 'Заполнить список заново':
            self.refill_absentees(message)
        elif message.text == 'Выбрать присутствующих':
            self.bot.send_message(message.chat.id, "Выбрать присутствующих:", reply_markup=self.generate_keyboard())
        elif message.text in self.absentees:
            self.remove_absentee(message)
        elif message.text == 'Вернуться на /start':
            self.start(message)
        else:
            self.bot.send_message(message.chat.id, "Неизвестная команда. Используйте кнопки для взаимодействия.")

    def remove_absentee(self, message):
        removed_name = message.text
        self.absentees.remove(removed_name)
        self.bot.send_message(message.chat.id, "Выбрать присутствующих:", reply_markup=self.generate_keyboard())

    def setup_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def handle_start(message):
            self.start(message)

        @self.bot.message_handler(commands=['absentees'])
        def handle_absentees(message):
            self.show_absentees(message)

        @self.bot.message_handler(commands=['fill'])
        def handle_fill(message):
            self.refill_absentees(message)

        @self.bot.message_handler(func=lambda message: True)
        def handle_all_messages(message):
            self.handle_buttons(message)

    def run(self):
        self.bot.polling()

if __name__ == "__main__":
    bot = AbsenteeBot(TOKEN)
    bot.run()