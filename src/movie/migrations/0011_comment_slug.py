# Generated by Django 3.0.3 on 2020-02-24 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_auto_20200223_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
