from django.db import models
from django.contrib.auth.models import User


class Account (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    avatar = models.ImageField(upload_to = "avatars/")

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
    
    def __str__(self):
        return self.user.username


# Create your models here.
