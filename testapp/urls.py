from django.conf.urls import url

from testapp import views
from testapp.next import testviews

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^next/', testviews.next),
]