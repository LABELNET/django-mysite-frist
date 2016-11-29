from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


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


#初始化token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
