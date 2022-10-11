
from django.db import models
from django.conf import settings


class Artiste(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    song = models.ForeignKey(
        'Song', null=True, blank=True, on_delete=models.SET_NULL)
    lyric = models.ForeignKey(
        'Lyric', related_name='leads', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'


class Song(models.Model):
    title = models.CharField(max_length=20)
    released_date = models.DateTimeField(auto_now_add=True)
    artiste_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def interaction_likes(self):
        return self.likes.count()


class Lyric(models.Model):
    content = models.CharField(max_length=100)
    song_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
