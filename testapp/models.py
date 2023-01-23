from django.db import models

class Trip(models.Model):
    origin= models.CharField(max_length=64)
    destination = models.CharField(max_length=64) 
    price = models.IntegerField()
    nights = models.IntegerField()


    def __str__(self):
        return self.origin + "->" + self.destination
# from django.db import models
# from mongoengine import *

# class Image(models.Model):
#     image = models.ImageField(upload_to='images/')
#     title = models.CharField(max_length=100)
#     description = models.TextField()
