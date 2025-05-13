import time

import requests
from bs4 import BeautifulSoup


def yandex_search(query):
    yandex_h1 = ''
    url = 'https://www.yandex.ru/yandsearch'

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Host': 'market.yandex.ru',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    }

    params = {
            'text': query,  # Поисковый запрос
            'lr': 213
    }

    response = requests.get(url=url, params=params, headers=headers)

    time.sleep(1.5)
    soup = BeautifulSoup(response.text, 'html.parser')
    for result in soup.find_all("h1"):
        yandex_h1 = result.get_text()

    return yandex_h1
