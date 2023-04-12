import requests
from bs4 import BeautifulSoup
from datetime import datetime


class Parcer():
    def __init__(self, year_search):
        self.year_search = year_search
        self.articles_list = []

    def parce_4pda(self):
        url = 'https://4pda.to/games/page/'
        page_number = 1
        year_of_article = 2023

        while year_of_article == self.year_search:
            response = requests.get(url + str(page_number))
            soup = BeautifulSoup(response.text, 'lxml')
            articles_on_page = soup.find_all('article', class_='post ufjEON')

            for count, article in enumerate(articles_on_page, 1):

                # Promoted articles labeled "green" aren't about games and have wrong text structure leading to error
                if article.find('span', class_='label green'):
                    continue

                res = {}
                res['title'] = article.find('h2', class_='list-post-title').text
                res['comments_amount'] = article.find('a', class_='v-count').text
                date_str = article.find('em', class_='date').text
                res['date'] = datetime.strptime(date_str, '%d.%m.%y').date()

                # Going deeper to the article link to extract full text
                article_url = article.find(itemprop='url')['href']
                response = requests.get(article_url)
                soup = BeautifulSoup(response.text, 'lxml')

                text_full = soup.find('div', class_='content-box').text
                # Getting rid of empty lines and last part like "source: youtu.be"
                res['article'] = ' '.join([s for s in text_full.split('\n') if s][:-1])

                if res['date'].year == self.year_search and count <= 20:
                    # ArticleData.save(title=title, date=date, comments_amount=comments_amount, article=text_clear)
                    self.articles_list.append(res)
                    print(count, end=' ')
                else:
                    break

            year_of_article = 2022  # temp solution to test small amounts
            # year_of_article = date.year
            page_number += 1
