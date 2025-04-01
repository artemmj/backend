from rest_framework import serializers

from apps.article.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'created_at', 'title', 'body')
