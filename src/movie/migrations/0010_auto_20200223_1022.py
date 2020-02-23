# Generated by Django 3.0.3 on 2020-02-23 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_auto_20200223_1018'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Watch_Links',
            new_name='Watch_Link',
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('romance', 'ROMANCE'), ('drama', 'DRAMA'), ('action', 'ACTION'), ('comedy', 'COMEDY')], max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('ra', 'Recently Added'), ('tr', 'Top Rated'), ('mw', 'Most Watched')], max_length=2),
        ),
    ]