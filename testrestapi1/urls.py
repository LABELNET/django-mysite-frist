from django.conf.urls import url

from .views import PartyList, PersonList

urlpatterns = [
    url(r'^list/', PartyList.as_view()),
    url(r'^api/', PersonList.as_view()),
]
