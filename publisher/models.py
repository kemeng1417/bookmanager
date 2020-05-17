from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=32)



class Book(models.Model):
    name = models.CharField(max_length=32)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
