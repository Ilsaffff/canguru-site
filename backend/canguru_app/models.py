from django.db import models
from django import forms
from mptt.models import MPTTModel, TreeForeignKey


class User(models.Model):
    first_name = models.CharField(verbose_name='Имя', db_index=True, max_length=64)
    last_name = models.CharField(verbose_name='Фамилия', max_length=64)
    username = models.CharField(verbose_name='Никнейм', max_length=64)
    date_of_birth = models.DateField(verbose_name='Дата рождения', max_length=16, null=True)
    password = models.CharField(verbose_name='Пароль', max_length=64, null=True)

    def __str__(self):
        return self.username
