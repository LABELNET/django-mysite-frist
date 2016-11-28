from django.db import models


# Create your models here.
class Party(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    title = models.CharField(max_length=50, default='this is a party')
    address = models.CharField(max_length=50, default="ShangHai")
    is_off = models.BooleanField(default=False)
    link = models.CharField(max_length=200, default="http://www.baidu.com")

    class Meta:
        ordering = ('create_date',)
