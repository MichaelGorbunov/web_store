from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/', null=True, blank=True, verbose_name='Изображение')
    created_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    published = models.BooleanField(verbose_name='Статус публикации', default=True)
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
