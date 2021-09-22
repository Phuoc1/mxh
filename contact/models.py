from django.db import models

# Create your models here.
class contactForm(models.Model):
    usernam = models.CharField(max_length=25)
    email = models.EmailField()
    body = models.TextField()