from django.db import models
from uuid import uuid4


class Comment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    content = models.TextField(verbose_name='Содержимое')
    published_date = models.DateTimeField(verbose_name='Дата публикации')
    author = models.CharField(max_length=141)
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
    image = models.CharField(max_length=1000)
    country_code = models.CharField(max_length=3)
    rocket_id = models.ForeignKey('Rocket', on_delete=models.CASCADE)
    pad_id = models.ForeignKey('Pad', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Rocket(models.Model):
    class Meta:
        verbose_name = 'Космический аппарат'
        verbose_name_plural = 'Космические аппараты'

    rocket_name = models.CharField(max_length=600)

    def __str__(self):
        return self.rocket_name


class Pad(models.Model):
    class Meta:
        verbose_name = 'Космодром'
        verbose_name_plural = 'Космодромы'

    wiki_url = models.CharField(max_length=600)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    total_launch_count = models.IntegerField()
