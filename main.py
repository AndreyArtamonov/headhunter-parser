import requests
from lxml import html
import re
import database
import sys

title = "Парсер данных о вакансиях"

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/100.0.4896.88 Safari/537.36 '
}


def has_count_vacancies(page):
    return len(page) == 2


def get_number_vacancies(keywords):
    mask = '//h1[@class="bloko-header-section-3"]/text()'

    for value in keywords:
        url = 'https://hh.ru/search/vacancy?text=' + value[1]
        page = html.fromstring(requests.get(url, headers=headers).text).xpath(mask)

        if has_count_vacancies(page):
            count = int(re.sub(r"\s+", "", page[0]))
            values = (value[0], count)
        else:
            values = (value[0], 0)

        database.save_stats(values)

        print(value[1] + ' [' + str(values[1]) + ']')


def parse_stats():
    keywords = database.get_keywords()

    if len(keywords) > 0:
        print('===Получаем все ключевые слова для поиска из базы данных===')
        get_number_vacancies(keywords)
        print('===Парсинг данных завершен===')
    else:
        print('===Добавьте ключевые слова в базу данных===')


if __name__ == '__main__':
    # TODO: Добавить исключение, если не добавлены аргументы
    if sys.argv[1] == '--parse-stats':
        parse_stats()
    else:
        print('===Не переданы параметры для запуска===')
