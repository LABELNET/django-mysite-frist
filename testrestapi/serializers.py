from rest_framework import serializers

from .models import Party


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        field = ('id', 'create_date', 'content', 'title', 'address', 'is_off', 'link')