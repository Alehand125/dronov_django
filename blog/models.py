from django.db import models
from django.contrib import admin


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Текст")
    timestamp = models.DateTimeField(verbose_name="Дата")
    email = models.EmailField(verbose_name="Электронная почта")

    class Meta:
        ordering = ("-timestamp",)

        verbose_name = 'Пост'
        verbose_name_plural = "Посты"

