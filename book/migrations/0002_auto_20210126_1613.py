# Generated by Django 3.1.4 on 2021-01-26 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='is_closed',
        ),
        migrations.RemoveField(
            model_name='book',
            name='is_favorite',
        ),
    ]
