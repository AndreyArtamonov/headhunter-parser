import sqlite3
import os

if os.path.exists('database.sqlite3'):
    print('===Соединение с базой данных===')
    database = sqlite3.connect('database.sqlite3')
else:
    print('===Создаем базу данных===')
    open('database.sqlite3', 'a').close()
    database = sqlite3.connect('database.sqlite3')
    database.execute("CREATE TABLE keywords (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR (255) NOT NULL)")
    database.execute(
        "CREATE TABLE stats (id INTEGER  PRIMARY KEY AUTOINCREMENT, keyword_id INTEGER  REFERENCES keywords (id), "
        "value INTEGER NOT NULL DEFAULT (0), created_at DATETIME DEFAULT((datetime('now'))))")
    database.commit()


def get_keywords():
    return database.execute('SELECT * from keywords').fetchall()


def save_stats(values):
    database.execute('INSERT INTO stats(keyword_id, value) VALUES(?, ?)', values)
    database.commit()
