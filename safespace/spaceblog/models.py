from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    post_heading = models.CharField(max_length=200)
    post_text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")

    def __str__(self):
        return self.post_heading


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
