import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GameStat.settings')
django.setup()

from GameData.parcing import Parcer
from GameData.models import ArticleData, VideoGame
from django.db.models import Count, Sum


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


def link_games_to_articles(videogame_titles, articles):
    """Checking if any game from list is in the article and link it adding to database"""
    for article in articles:
        for videogame in videogame_titles:
            if article.article.find(videogame.title) > 0:
                res = ArticleData(pk=article.id)
                res.videogame = VideoGame(pk=videogame.id)
                res.save(update_fields=['videogame'])   # it allows rewriting only targeted field


def rate_videogame_frequency(top):
    """Getting statistics how frequency a videogame appears in all articles.
    Filtering videogames to leave only ones that appear in articles to optimize process"""

    rating = VideoGame.objects\
        .filter(articledata__videogame__gte=1)\
        .annotate(Count('articledata'))\
        .order_by('-articledata__count')

    print('Leaderboard of appearance frequency:')
    for elem in rating[:top]:
        print(f"{elem.title}: {elem.articledata__count}")

def rate_videogame_discussions(top):
    """Getting statistics how many comments a videogame have through all related articles.
    Filtering videogames to leave only ones that appear in articles to optimize process"""

    rating = VideoGame.objects\
        .filter(articledata__videogame__gte=1)\
        .annotate(total_comments=Sum('articledata__comments_amount'))\
        .order_by('-total_comments')

    print('Leaderboard of comments amount:')
    for elem in rating[:top]:
        print(f"{elem.title}: {elem.total_comments}")

ArticleData.objects.all().delete()
parcing_articles = Parcer()
parcing_articles.parce_4pda(2023, 4, 28)
update_database_with_articles(parcing_articles.articles_list)

videogame_titles = VideoGame.objects.all()
articles = ArticleData.objects.all()
link_games_to_articles(videogame_titles, articles)

rate_videogame_frequency(top=5)
rate_videogame_discussions(top=5)