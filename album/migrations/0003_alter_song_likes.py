# Generated by Django 4.1.2 on 2022-10-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_artiste_lyric_artiste_song_remove_song_likes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
