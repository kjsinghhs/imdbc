# Generated by Django 3.0.3 on 2020-02-20 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20200218_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('romance', 'ROMANCE'), ('drama', 'DRAMA'), ('comedy', 'COMEDY'), ('action', 'ACTION')], max_length=10),
        ),
    ]