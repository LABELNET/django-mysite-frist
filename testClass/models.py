from datashape import Date
from django.db import models

food_default_name = "锅巴"


class Food(models.Model):
    iis_code = models.CharField(max_length=32, default='mysite')
    name = models.CharField(max_length=20, default=food_default_name)
    price = models.IntegerField()
    create_date = models.DateField(auto_now_add=Date.cls)