# Generated by Django 3.2.9 on 2021-12-04 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_list_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='movies',
            field=models.ManyToManyField(blank=True, to='movie.Movie'),
        ),
    ]
