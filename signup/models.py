from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    DOB=models.CharField(max_length=20)
    Mobile=models.BigIntegerField(default=0)
