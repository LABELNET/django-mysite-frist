from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Party


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('id', 'create_date', 'content', 'title', 'address', 'is_off', 'link')


"""
全部字段 ：fields = '__all__'
个别字段 ：fields = ('id', 'create_date', 'content', 'title', 'address', 'is_off', 'link')
"""


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        name = validated_data['username']
        ipass = validated_data['password']
        user = User(username=name)
        user.set_password(ipass)
        user.save()
        return user
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
