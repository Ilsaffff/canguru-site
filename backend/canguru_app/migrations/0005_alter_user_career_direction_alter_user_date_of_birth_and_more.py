# Generated by Django 4.1.5 on 2023-01-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canguru_app', '0004_user_career_direction_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='career_direction',
            field=models.CharField(choices=[('PR', 'Product Management')], max_length=2, null=True, verbose_name='Карьерное направление'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(max_length=16, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(db_index=True, max_length=64, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=64, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=64, verbose_name='Никнейм'),
        ),
    ]
