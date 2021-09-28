import requests
from bs4 import BeautifulSoup

KEYWORDS = {'дизайн', 'фото', 'web', 'Python'}
URL = 'https://habr.com/ru/all/'


def scrapping(keywords, url):
    response = requests.get(url)
    response.raise_for_status()
    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    articles = soup.find_all("article")
    for article in articles:
        hubs = article.find_all('div', class_='tm-article-snippet')
        hubs_text = [hub.text for hub in hubs]
        hubs_text = {x for s in hubs_text for x in s.split()}
        if keywords & hubs_text:
            title = article.find('h2')
            link = title.find('a').attrs.get('href')
            url = 'https://habr.com' + link
            date = article.find('time').attrs.get('title')
            return print(f'{date} - {title.text} - {url}')


if __name__ == '__main__':
    scrapping(KEYWORDS, URL)
