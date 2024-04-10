from django.db import models

# Create your models here.
class School(models.Model):
    sname = models.CharField(max_length=50, primary_key=True)
    sprincipal = models.CharField(max_length=50)
    scontact = models.CharField(max_length=50)

class Student(models.Model):
    sname = models.ForeignKey(School,on_delete=models.CASCADE)
    stdname = models.CharField(max_length=50)
    stdage = models.IntegerField()