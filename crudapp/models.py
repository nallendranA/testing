from django.db import models
class Student(models.Model):
    sno=models.IntegerField()
    name=models.CharField(max_length=64)
    age=models.IntegerField()
    dep=models.CharField(max_length=25)

# Create your models here.
