from django.conf.urls import url
from rest_framework.authtoken import views

from .views import PartyDetail, UserList
from .views import PartyList
from .views import PartyListSet

party_set_list = PartyListSet.as_view({
    'get': 'list',
})

urlpatterns = [
    url(r'^list/', PartyList.as_view()),
    url(r'^listset/', party_set_list),
    url(r'^detail/(?P<pk>[0-9]+)$', PartyDetail.as_view()),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^userlist/', UserList.as_view()),
]
