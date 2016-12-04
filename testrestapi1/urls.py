from django.conf.urls import url

from .views import PartyList, PersonList, PersonListRespnse, PersonList1

urlpatterns = [
    url(r'^list/', PartyList.as_view()),
    url(r'^api/', PersonList.as_view()),
    url(r'^json/', PersonListRespnse.as_view()),
    url(r'^list1/', PersonList1.as_view()),
]
