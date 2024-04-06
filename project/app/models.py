from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    Profile_pic = models.ImageField()
    
    def __str__(self):
        return self.username.username