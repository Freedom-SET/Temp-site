from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=20)
    semester = models.CharField(max_length=3, null=True)
    email = models.EmailField(primary_key=True)
    phone = models.CharField(max_length=10, unique=True)
    usn = models.CharField(max_length=11, unique=True)
    interests = models.CharField(max_length=200)
    personal_statement = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
