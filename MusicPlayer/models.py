from django.db import models


class Musics(models.Model):
    musicId = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.CharField(null=False, max_length=250)
    singer = models.CharField(null=False, max_length=50)
    writer = models.CharField(null=False, max_length=50)
    musicThumbnail = models.FileField(upload_to="media/", null=True, default=None)
    musicFile = models.FileField(upload_to="media/", null=True, default=None)
    medium = models.CharField(default='Hindi', max_length=10)
    type = models.CharField(default='Romantic', max_length=10)


class User(models.Model):
    Username = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(null=False, max_length=20)
    name = models.CharField(null=False, max_length=30)
    email = models.CharField(null=False, max_length=50)
    mobile = models.ImageField(default=0)
