from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey


class VideoGame(models.Model):
    title = models.CharField(max_length=50, unique=True, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class ArticleData(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    comments_amount = models.IntegerField(blank=True, null=True)
    article = models.TextField(default='')
    user = ForeignKey(User, verbose_name='User', on_delete=models.SET_NULL, blank=True, null=True)
    videogame = ForeignKey(VideoGame, on_delete=models.SET_NULL, blank=True, null=True)



