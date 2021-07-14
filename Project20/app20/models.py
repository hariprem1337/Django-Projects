from django.db import models

class StudentRegisterModel(models.Model):
    number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    email = models.EmailField(unique=True, max_length=40, null=False)
    contact = models.IntegerField(unique=True, null=False)
    photo = models.ImageField(upload_to='student_images/')
    dob = models.DateField(null=False)
    location = models.CharField(max_length=30, null=False)
    date_of_reg = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=30, null=False, default=0000)
