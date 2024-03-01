import requests
from bs4 import BeautifulSoup as BS

URL = "https://cinematica.kg"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}


def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


def get_data(html):
    bs = BS(html, "html.parser")
    items = bs.find_all("div", class_='movies-grid')
    cinematica_list = []
    for item in items:
        title = item.find("div", class_="movie-title").get_text(strip=True)
        image = item.find("div", class_="movie-poster").find("img").get("src")
        cinematica_list.append({"title": title, "image": image})

    return cinematica_list


def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        cinematica_list_2 = []
        for page in range(1, 3):
            response = get_html(f'https://cinematica.kg/movies/', params={'page': page})
            cinematica_list_2.extend(get_data(response.text))
        return cinematica_list_2

    else:
        raise Exception('Ошибка при парсинге')



# print(parsing())