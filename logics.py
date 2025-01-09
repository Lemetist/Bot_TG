import pandas as pd
import datetime

# Инициализация данных
data = {
    "ФИО": [
        "Алаторцев П.В.", "Багиров Э.Э.", "Башкиров И.В.", "Борхоев Б.Б.", "Евстафьев А.А.",
        "Журавлева М.Р.", "Киреев А.А.", "Ламажап Н.А.", "Ленючев Д.А.", "Львов М.Д.",
        "Макаров Е.С.", "Овчинникова И.А.", "Подлинный М.В.", "Сатин Т.С.", "Секункова П.А.",
        "Семечаевский П.В.", "Сержантов И.А.", "Токарев А.Д.", "Чичёв А.Б.", "Шахкиримов К.И.",
        "Шишалов С.Д.", "Максимов М.М.", "Маковский А.С."
    ],
    "Понедельник": [None] * 23,
    "Вторник": [None] * 23,
    "Среда": [None] * 23,
    "Четверг": [None] * 23,
    "Пятница": [None] * 23,
    "Суббота": [None] * 23,
}

# Функция обновления списка отсутствующих
def reforming_list(absentees: list):
    today = datetime.date.today()
    weekday = today.weekday()
    # Преобразуем номер дня недели в строку
    weekday_names = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
    weekday_name = weekday_names[weekday]
    # Отмечаем отсутствующих
    for i, name in enumerate(data["ФИО"]):
        if name in absentees:
            data[weekday_name][i] = "н"

# Сохранение данных в Excel
def save_to_excel(data, file_path="ИСП11-322АП.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
    print(f"Файл сохранен как: {file_path}")

# Пример использования
absentees_list = ["Алаторцев П.В.", "Журавлева М.Р.", "Шахкиримов К.И."]
reforming_list(absentees_list)
save_to_excel(data)
