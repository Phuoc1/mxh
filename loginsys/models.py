from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Newuser(models.Model):
    Username=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    Pwd=models.CharField(max_length=150)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=1)
    Martialstatus=models.CharField(max_length=150)

