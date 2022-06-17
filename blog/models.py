from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
