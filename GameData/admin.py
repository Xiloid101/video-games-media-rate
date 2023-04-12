from django.contrib import admin
from .models import ArticleData, VideoGame


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "date",)


class VideoGameAdmin(admin.ModelAdmin):
    list_display = ('title',)

    # @admin.display(ordering='title')  # allowing to order in Admin, not in DB itself
    # def game_title(self, obj):
    #     return obj.game_title


admin.site.register(ArticleData, ArticleAdmin)
admin.site.register(VideoGame)
