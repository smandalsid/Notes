from django.db import models
from users.models import CustomUser
from django.contrib.auth import get_user_model
# Create your models here.

class Note(models.Model):
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    uploaddata = models.CharField(max_length=30)
    branch = models.CharField(max_length=20)
    subject = models.CharField(max_length=30)
    notesfile = models.FileField()
    filetype = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.author.username