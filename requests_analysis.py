import pandas
from ya_search import yandex_search
from itertools import chain
import re
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# import time
# from datetime import timedelta


# start_time = time.monotonic()
# end_time = time.monotonic()
# time_script = timedelta(seconds=end_time - start_time)
# nltk.download('punkt_tab')

# создание списка из файла вместо цикла for
# requests = df.apply(lambda row: row['СтрокаЗапроса'], axis=1).to_list()

chars = [')', '(', ',', '–', '*', '"', '%', ';', ':', '{', '}', '@', '=', '#', '№', '!', '_', '¶', '°', '+']


def requests_analysis():
    bad_words = []
    requests_list = []
    list_list_words = []
    list_list_words_without_characters = []
    list_products = []
    data = pandas.read_excel("2025-04-28 Запросы B2B.xlsx", engine='openpyxl')
    df = pandas.DataFrame(data)

    for row in df.itertuples():
        requests_list.append(row[1])

    # разбиваем CamelCase слова и разбиваем весь поисковой запрос на слова
    for i in requests_list:
        list_list_words.append((re.sub(r'([a-z])([A-Z])', r'\1 \2', str(i))).split())

    # удаляем символы в словах
    for list_words in list_list_words:
        for word in list_words:
            if any(s in word for s in chars):
                bad_words.append(word)
        for bad_word in bad_words:
            if bad_word in list_words:
                list_words.remove(bad_word)
        list_list_words_without_characters.append(list_words)

    # объединяем слова в списках в запрос
    list_requests_without_characters = [[' '.join(n)] for n in list_list_words_without_characters]
    list_requests_without_doubles = list(set(chain.from_iterable(list_requests_without_characters)))

    # подключаем функцию отправки запроса в поиск яндекса
    # for product in list_requests_without_doubles:
    #     if len(yandex_search(query=product)) != 0 or yandex_search(query=product) != '':
    #         list_products.append(yandex_search(query=product))
    #     else:
    #         list_products.append(product)

    # записываем результат в файл
    with open('result.txt', 'w', encoding='utf-8') as file:
        for request in list_requests_without_doubles:
            file.write(f'{str(request)}\n')


requests_analysis()
