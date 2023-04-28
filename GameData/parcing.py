import requests
from bs4 import BeautifulSoup
import datetime

class Parcer():
    def __init__(self):
         self.articles_list = []

    def parce_4pda(self, year, month, day):
        self.end_date = datetime.datetime(year, month, day)
        url = 'https://4pda.to/games/page/'
        page_number = 1
        date_of_article = self.end_date

        while date_of_article >= self.end_date:
            response = requests.get(url + str(page_number))
            soup = BeautifulSoup(response.text, 'lxml')
            articles_on_page = soup.find_all('article', class_='post ufjEON')

            for count, article in enumerate(articles_on_page, 1):
                """Going through articles within the page"""

                # Promoted articles labeled "green" aren't about games and have wrong text structure leading to error
                if article.find('span', class_='label green'):
                    continue

                res = {}
                res['title'] = article.find('h2', class_='list-post-title').text
                res['comments_amount'] = article.find('a', class_='v-count').text
                date_str = article.find('em', class_='date').text
                res['date'] = datetime.datetime.strptime(date_str, '%d.%m.%y')

                # Going deeper to the article link to extract full text
                article_url = article.find(itemprop='url')['href']
                response = requests.get(article_url)
                soup = BeautifulSoup(response.text, 'lxml')

                text_full = soup.find('div', class_='content-box').text
                # Getting rid of empty lines and last part like "source: youtu.be"
                res['article'] = ' '.join([s for s in text_full.split('\n') if s][:-1])

                if res['date'] >= self.end_date:
                    self.articles_list.append(res)
                    print(count, end=' ')
                else:
                    break
            print() # make a new line for checked articles counter
            date_of_article = res['date']
            page_number += 1
