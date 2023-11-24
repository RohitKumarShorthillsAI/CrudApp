from django.db import models

# Create your models here.

class Student(models.Model): # the name of class represent table name in database
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    roll_number = models.IntegerField()
    section = models.CharField(max_length=3)