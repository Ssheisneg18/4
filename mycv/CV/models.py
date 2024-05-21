from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField()
    phone = models.CharField(max_length= 20) #optional
    summary = models.TextField(max_length= 250, editable= True)
    skills = models. TextField()
    experience = models.TextField()