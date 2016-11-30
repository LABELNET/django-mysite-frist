from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20, default='Lao')
    weight = models.FloatField()
    height_cm = models.IntegerField()
