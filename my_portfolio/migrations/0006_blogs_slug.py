# Generated by Django 4.1.6 on 2023-02-07 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0005_blogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='slug',
            field=models.SlugField(max_length=256, null=True),
        ),
    ]
