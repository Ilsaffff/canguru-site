from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class User(models.Model):
    first_name = models.CharField(verbose_name='Имя', db_index=True, max_length=64)
    last_name = models.CharField(verbose_name='Фамилия', max_length=64)
    username = models.CharField(verbose_name='Никнейм', max_length=64)
    date_of_birth = models.DateField(verbose_name='Дата рождения', max_length=16, null=True)

    CAREER_DIRECTION_CHOICES = [
        ('PR', 'Product Management')
    ]

    career_direction = models.CharField(verbose_name='Карьерное направление', max_length=2,
                                        choices=CAREER_DIRECTION_CHOICES, null=True)

    def __str__(self):
        return self.username
