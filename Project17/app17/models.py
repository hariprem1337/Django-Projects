from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40, unique=True)
    contact = models.IntegerField(max_length=15, unique=True)
    location = models.CharField(max_length=30)
    password =models.CharField(max_length=30)
