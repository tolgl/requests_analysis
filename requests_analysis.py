import pandas
from ya_search import yandex_search
from itertools import chain
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

# запись в файл
# with open('result.txt', 'w', encoding='utf-8') as file:
#     for request in requests_list:
#         file.write(f'{str(request)}\n')

chars = [')', '(', ',', '–', '*', '"', '%', '/', ';', ':', '{', '}', '@', '=', '#', '№', '!', '_', '¶', '°', '+']


def requests_analysis():
    bad_words = []
    requests_list = []
    list_list_words = []
    list_list_words_without_characters = []
    list_products = []
    list_products_2 = []
    data = pandas.read_excel("2025-04-28 Запросы B2B — копия.xlsx", engine='openpyxl')
    df = pandas.DataFrame(data)

    for row in df.itertuples():
        requests_list.append(row[1])

    hhh = [
        'AURORA Интеллектуальное зарядное устройство SPRINT-6 (148 )вывыв %1fdsfs',
        'Уголок крепежный  оцинкованный 100х100х100х 2,5 мм – 293шт (ГОСТ 14918-2020)'
    ]

    for i in requests_list:
        list_list_words.append(str(i).lower().split())

    for list_words in list_list_words:
        for word in list_words:
            if any(s in word for s in chars):
                bad_words.append(word)
        for bad_word in bad_words:
            if bad_word in list_words:
                list_words.remove(bad_word)
        list_list_words_without_characters.append(list_words)

    # print(list_list_words_without_characters)
    list_requests_without_characters = [[' '.join(n)] for n in list_list_words_without_characters]
    print(list_requests_without_characters)

    for product in chain.from_iterable(list_requests_without_characters):
        if len(yandex_search(query=product)) != 0:
            list_products.append(yandex_search(query=product))
        else:
            list_products_2.append(product)

    print(list_products)
    print(list_products_2)


requests_analysis()
