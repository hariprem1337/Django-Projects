from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40, unique=True)
    contact = models.IntegerField(unique=True)
    location = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
