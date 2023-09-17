from django.db import models
from datetime import date
from django.urls import reverse
from django.utils import timezone




class News(models.Model):
    title = models.CharField('Название', max_length=150)
    description = models.CharField('Описание', max_length=400)
    image = models.ImageField('Изображение', upload_to='news/')
    slug = models.SlugField(max_length=150, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'