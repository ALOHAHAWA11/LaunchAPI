from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class Comment(models.Model):

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    content = models.TextField(verbose_name='Содержимое')
    published_date = models.DateTimeField(verbose_name='Дата публикации')
    author = models.CharField(max_length=140)
    launch = models.ForeignKey('Launch', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.content


class Launch(models.Model):

    class Meta:
        verbose_name = 'Запуск'
        verbose_name_plural = 'Запуски'

    id = models.UUIDField(primary_key=True, default=uuid4, editable=True)
    name = models.CharField(max_length=600, verbose_name='Имя запуска')
    window_start = models.DateTimeField(verbose_name='Дата запуска')
    window_end = models.DateTimeField(verbose_name='Дата окончания запуска')

    def __str__(self):
        return self.name

