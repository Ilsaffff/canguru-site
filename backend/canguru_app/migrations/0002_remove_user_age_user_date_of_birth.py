# Generated by Django 4.1.5 on 2023-01-17 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canguru_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(max_length=8, null=True),
        ),
    ]
