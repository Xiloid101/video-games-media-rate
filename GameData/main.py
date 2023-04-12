import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GameStat.settings')
django.setup()

from GameData.parcing import Parcer
from GameData.models import ArticleData, VideoGame


def update_database_with_articles(articles_list):   # To add check if all fields exist
    """Takes article list and save articles to DB one by one"""
    for article in articles_list:
        data = ArticleData(
            title=article['title'],
            date=article['date'],
            article=article['article'],
            comments_amount=article['comments_amount'],
        )
        data.save()


def link_games_to_articles(games, articles):
    """Checking if any game from list is in the article and link it adding to database"""
    for article in articles:
        for videogame in videogame_titles:
            if article['article'].find(videogame['title']) > 0:
                res = ArticleData(pk=article['id'])
                res.videogame = VideoGame(pk=videogame['id'])
                res.save(update_fields=['videogame'])   # it allows rewriting only targeted field


ArticleData.objects.all().delete()

parcing_articles = Parcer(year_search=2023)
parcing_articles.parce_4pda()
update_database_with_articles(parcing_articles.articles_list)

videogame_titles = VideoGame.objects.values('id', 'title')
articles = ArticleData.objects.values('id', 'article')
link_games_to_articles(videogame_titles, articles)

