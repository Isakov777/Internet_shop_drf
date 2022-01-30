from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    

    username = models.CharField(max_length=255, unique=True)
    profile = models.ImageField(upload_to = 'profiles', blank = True, null = True)
    age = models.PositiveBigIntegerField(default=0)
