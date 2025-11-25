FROM python:3.11-slim

WORKDIR /app

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Копирование requirements и установка Python зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода приложения
COPY ПОЛИРОЛЬОТБИВКИ.py .
COPY config.py* ./
COPY templates/ ./templates/

# Создание директорий для данных
RUN mkdir -p secrets/user_data generated

# Запуск бота
CMD ["python", "ПОЛИРОЛЬОТБИВКИ.py"]

