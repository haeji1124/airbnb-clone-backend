from django.db import models
from django.contrib.auth.models import User

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Tweet(TimeStampedModel):
    payload = models.TextField(max_length=180)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}: {self.payload[:20]}..."

class Like(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} likes {self.tweet.payload[:20]}..."