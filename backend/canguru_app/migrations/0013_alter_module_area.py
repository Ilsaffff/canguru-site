# Generated by Django 4.1.5 on 2023-01-22 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('canguru_app', '0012_alter_module_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='canguru_app.area'),
        ),
    ]