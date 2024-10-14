import pandas as pd
import datetime
data = {
    "ФИО": [
        "Алаторцев П.В.","Багиров Э.Э.","Башкиров И.В.","Борхоев Б.Б.","Евстафьев А.А.","Журавлева М.Р.","Киреев А.А.","Ламажап Н.А.","Ленючев Д.А.","Львов М.Д.","Макаров Е.С.","Овчинникова И.А.","Подлинный М.В.","Сатин Т.С.","Секункова П.А.","Семечаевский П.В.","Сержантов И.А.","Токарев А.Д.","Чичёв А.Б.","Шахкиримов К.И.","Шишалов С.Д.","Максимов М.М.","Маковский А.С."
    ],
    "Понедельник" : None,
    "Вторник": None,
    "Среда": None,
    "Четверг": None,
    "Пятница": None,
    "Суббота": None,
}

def reforming_list(absentees: list):
    today = datetime.date.today()
    weekday = today.weekday()
    # Преобразуем номер дня недели в строку
    weekday_names = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
    weekday_name = weekday_names[weekday]
    for i, name in enumerate(data["ФИО"]):
        for day in [weekday_name]:
            if name in absentees:
                if data[day] is None:
                    data[day] = [None] * len(data["ФИО"])
                data[day][i] = "н"


def save_to_excel(data, file_path="ИСП11-322АП.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
    print(f"Файл сохранен как: {file_path}")


save_to_excel(data)