from django.conf.urls import url

from .views import PartyDetail
from .views import PartyList

urlpatterns = [
    url(r'^list/', PartyList.as_view()),
    url(r'^detail/(?P<pk>[0-9]+)$', PartyDetail.as_view())
]
