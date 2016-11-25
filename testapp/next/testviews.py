from django.http import HttpResponse


# Create your views here.
def next(request):
    return HttpResponse("TestApp next")