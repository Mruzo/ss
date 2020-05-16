from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    post_heading = models.CharField(max_length=200)
    post_text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")

    def __str__(self):
        return self.post_heading

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
