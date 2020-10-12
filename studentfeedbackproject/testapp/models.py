from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=64)
    rollno=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=64)
    rpassword=models.CharField(max_length=64)
    feedback=models.TextField()
