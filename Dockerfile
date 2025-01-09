FROM python:3.13-slim

# Установите рабочую директорию
WORKDIR /app

# Копирование и установка зависимостей
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копирование приложения в контейнер
COPY . .

# Запуск приложения
CMD ["python3", "main.py"]