from django.db import models


# Create your models here.
class StoreInfo(models.Model):
    name = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=50, default="China")

    def __str__(self):
        return self.name + self.address