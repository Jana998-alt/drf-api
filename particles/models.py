from django.db import models
from django.db.models.fields import TextField
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

# Create your models here.

class Particle(models.Model):
    name = models.TextField(max_length= 64)
    auther = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    charge =  models.TextField()
    type = models.TextField()
    
    def __str__(self):
        return self.name