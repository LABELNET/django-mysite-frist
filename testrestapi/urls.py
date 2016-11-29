from django.conf.urls import url

from .views import PartyDetail
from .views import PartyList
from .views import PartyListSet

party_set_list = PartyListSet.as_view({
    'get': 'list',
})

urlpatterns = [
    url(r'^list/', PartyList.as_view()),
    url(r'^listset/', party_set_list),
    url(r'^detail/(?P<pk>[0-9]+)$', PartyDetail.as_view())
]