from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    ROOM_TYPES = (
        (1, 'Single'),
        (2, 'Double'),
        (3, 'Triple'),
    )

    STATUS = (
        (1, 'Occupied'),
        (2, 'Empty'),
    )

    name = models.CharField(max_length=50)
    status = models.PositiveSmallIntegerField(choices=STATUS)
    room_number = models.IntegerField(blank=True, null=True)
    nobeds = models.IntegerField(blank=True, null=True)
    room_type = models.PositiveSmallIntegerField(choices=ROOM_TYPES)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __unicode__(self):
        return self.text+' - '+self.author.username


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    actors = models.ManyToManyField(Actor)
    year = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
