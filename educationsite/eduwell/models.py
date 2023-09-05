from datetime import datetime
from django.db import models

# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    path = models.ImageField (upload_to="images/")
    date_create = models.DateTimeField(default=datetime.now, blank= True)

class Discipline(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    path = models.ImageField (upload_to="images/") 
    link = models.TextField()
    date_create = models.DateTimeField(default=datetime.now, blank= True)


class Banner(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    path = models.ImageField (upload_to="media/")
    button = models.TextField()
    date_create = models.DateTimeField(default=datetime.now, blank= True) 