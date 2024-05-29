from django.db import models
from django.contrib.auth.models import User as AuthUser

class UserProfile(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=100, unique=True)
    email_address = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title
