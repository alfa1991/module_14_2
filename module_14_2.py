import sqlite3

# Создание базы данных и подключение к ней
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создание таблицы Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Заполнение таблицы 10 записями
users = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000),
]

cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users)

# Обновление balance у каждой 2-й записи, начиная с 1-й
cursor.execute('UPDATE Users SET balance = 500 WHERE id % 2 = 1')

# Удаление каждой 3-й записи, начиная с 1-й
cursor.execute('DELETE FROM Users WHERE id % 3 = 1')

# Удаление пользователя с id=6
cursor.execute('DELETE FROM Users WHERE id = 6')

# Подсчёт общего количества пользователей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

# Вывод среднего баланса на консоль
if total_users > 0:
    print(all_balances / total_users)
else:
    print("Нет пользователей для расчёта среднего баланса.")

# Закрытие соединения
connection.commit()
connection.close()
