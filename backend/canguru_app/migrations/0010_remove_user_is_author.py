# Generated by Django 4.1.5 on 2023-01-22 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canguru_app', '0009_user_is_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_author',
        ),
    ]
