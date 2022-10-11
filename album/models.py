
from django.db import models
from django.conf import settings


class Artiste(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name


class Song(models.Model):
    artiste_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    released_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_names='likes', blank=True)

    def __str__(self):
        return self.artiste_id.username

    @property
    def interaction_likes(self):
        return self.likes.count()

    class Meta:
        timestamp_of_song_release = ('-released_date')


class Lyric(models.Model):
    content = models.CharField(max_length=100)
    song_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_id.title
