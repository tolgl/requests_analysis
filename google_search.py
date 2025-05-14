import requests
from dotenv import load_dotenv
import os
load_dotenv()


def google_search(query):

    url = "https://www.googleapis.com/customsearch/v1"

    # Параметры запроса
    params = {
        'key': os.getenv('API_KEY'),  # Ваш API ключ
        'cx': os.getenv('CX'),  # Идентификатор вашей поисковой системы
        'q': query  # Поисковый запрос
    }
    pagemaps = []
    info_products = []
    name_products = []
    response = requests.get(url, params=params)

    if 'items' in response.json():
        for i in response.json()['items']:
            if 'pagemap' in i:
                pagemaps.append(i['pagemap'])
        for pagemap in pagemaps:
            if 'product' in pagemap:
                info_products.append(pagemap['product'])
        for info_product in info_products:
            if 'name' in info_product[0]:
                name_products.append(info_product[0]['name'])

    return name_products[0:1]
