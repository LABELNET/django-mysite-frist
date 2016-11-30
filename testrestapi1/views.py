from rest_framework import generics

from testrestapi.models import Party
from testrestapi.serializers import PartySerializer

# Create your views here.
from testrestapi1.models import Person
from testrestapi1.serializer import PersonSerializer


class PartyList(generics.ListCreateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
