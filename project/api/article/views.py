from rest_framework.viewsets import ModelViewSet

from apps.article.models import Article

from .serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
