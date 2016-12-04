from rest_framework import serializers

from testrestapi1.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class Person1Serializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20)
    weight = serializers.FloatField()
    height = serializers.IntegerField()

    # validate_fieId
    def validate_name(self, value):
        print('validate_name', type(value), value)
        return value

    def validate(self, attrs):
        print('validate', type(attrs), attrs)
        if attrs['weight'] > 100:
            raise serializers.ValidationError('your weight is too fat')
        return attrs

    def create(self, validated_data):
        print('create', type(validated_data), validated_data)
        height = validated_data['height']
        weight = validated_data['weight']
        name = validated_data['name']
        print(height)
        person = Person(name=name, weight=weight, height=height)
        person.save()
        return person

    def update(self, instance, validated_data):
        print('update', type(instance), instance, validated_data)
        instance.name = validated_data.get('name', instance.name)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.height_cm = validated_data.get('height', instance.height_cm)
        instance.save()
        return instance

    class Meta:
        model = Person
        fields = ('name', 'weight', 'height')
