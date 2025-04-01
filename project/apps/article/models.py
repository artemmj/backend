from django.db import models


class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField('Заголовок статьи', max_length=127)
    body = models.TextField('Тело статьи')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
