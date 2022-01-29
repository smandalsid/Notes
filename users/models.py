from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    regno = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    branch = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.username
