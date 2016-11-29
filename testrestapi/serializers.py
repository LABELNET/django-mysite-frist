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