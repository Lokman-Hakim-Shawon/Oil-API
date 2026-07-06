from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone=models.CharField(max_length=15,blank=True,null=True)
    Profile_image=models.URLField(blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.username
