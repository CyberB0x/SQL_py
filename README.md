
# 🗂️ User Management with MySQL and Python

## 📌 Описание
Этот проект представляет собой простую систему управления пользователями, реализованную на Python с использованием библиотеки `PyMySQL` для подключения к базе данных MySQL. Пользовательские данные (имя и email) сохраняются в базе данных `user_db`.

## ⚙️ Функциональность
- Подключение к базе данных MySQL
- Добавление новых пользователей в таблицу `users`
- Организация кода по модулям: `main.py`, `database.py`, `user.py`

## 🛠️ Стек технологий
- **Язык программирования:** Python 3
- **База данных:** MySQL
- **Библиотека для работы с БД:** PyMySQL
- **Среда разработки:** PyCharm
- **Дополнительно:** MySQL Workbench для управления базой данных

## 📁 Структура проекта
```
SQL_py/
│
├── main.py                 # Точка входа, добавление пользователей
├── app/
│   ├── __init__.py
│   ├── database.py         # Подключение к базе данных
│   └── user.py             # Логика добавления пользователя
└── venv/                   # Виртуальное окружение Python
```

## 🧩 Пример работы
```bash
$ python main.py
```
**Результат:** пользователь добавляется в базу данных `user_db`, таблицу `users`.

## 📌 Требования
- Установленный MySQL Server и MySQL Workbench
- Python 3.8+
- Установленный пакет `pymysql`:
```bash
pip install pymysql
```

## 📋 Пример SQL-запроса для создания таблицы
```sql
CREATE DATABASE user_db;

USE user_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);
```
