from rest_framework import serializers
from GameData.models import ArticleData


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ArticleData
        fields = "__all__"
