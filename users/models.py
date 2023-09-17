from django.db import models


class User(models.Model):
    name = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    studcode = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
         verbose_name = 'Студент'
         verbose_name_plural = 'Студенты'

