# Generated by Django 3.2.18 on 2023-04-24 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
