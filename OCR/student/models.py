from django.db import models

class RegistrationModel(models.Model):
    name = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=40, unique=True, null=False)
    contact = models.IntegerField(unique=True, null=False)
    password = models.CharField(max_length=30, null=False)
    otp = models.IntegerField(default=0000, null=False)
    status = models.CharField(default="pending", max_length=30, null=False)
    datetime = models.DateTimeField(auto_now_add=True)