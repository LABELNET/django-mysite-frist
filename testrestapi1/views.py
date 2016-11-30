from django.http import HttpResponse
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from mysite.util import JsonUtil
from testrestapi.models import Party
from testrestapi.serializers import PartySerializer
from testrestapi1.models import Person
from testrestapi1.serializer import PersonSerializer


class PartyList(generics.ListCreateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonListRespnse(APIView):
    def get(self, request):
        queryset = Person.objects.all()
        serializer = PersonSerializer(queryset, many=True)
        return JSONResponse(serializer.data)


Response

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        print(data)
        # values = (code = 110, msg = 'this is a test', data = data)
        # JSONSerializers()

        content = JSONRenderer().render(JsonUtil.params_data(110, "this a msg", data))
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
