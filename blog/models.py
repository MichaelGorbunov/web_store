from django.db import models
from unidecode import unidecode
from django.utils.text import slugify

def generate_unique_slug(klass, field):
    origin_slug = slugify(unidecode(field))
    unique_slug = origin_slug
    numb = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{origin_slug}-{numb}'
        numb += 1
    return unique_slug


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='photos/', null=True, blank=True, default="photos/default.jpg",verbose_name='Изображение')
    created_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    published = models.BooleanField(verbose_name='Статус публикации', default=True)
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    slug = models.SlugField(max_length=255,verbose_name="URL",null=False,unique=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_unique_slug(Post, self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

class Job(models.Model):
    job_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    # Add other fields as necessary
    interval = models.IntegerField(default=30)  # Interval in seconds
    # Add other fields as necessary

class CronJob(models.Model):
    job_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    minute = models.CharField(max_length=10, default='*')  # Cron format
    hour = models.CharField(max_length=10, default='*')    # Cron format
    day = models.CharField(max_length=10, default='*')     # Cron format
    month = models.CharField(max_length=10, default='*')   # Cron format
    day_of_week = models.CharField(max_length=10, default='*')  # Cron format

    def __str__(self):
        return self.name
