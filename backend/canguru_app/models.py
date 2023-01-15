from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.username
