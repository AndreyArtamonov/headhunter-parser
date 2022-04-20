import sqlite3

print('===Соединение с базой данных===')
database = sqlite3.connect('database.sqlite3')


def get_keywords():
    print('===Получаем все ключевые слова для поиска из базы данных===')
    return database.execute('SELECT * from keywords').fetchall()


def save_stats(values):
    database.execute('INSERT INTO stats(keyword_id, value) VALUES(?, ?)', values)
    database.commit()
