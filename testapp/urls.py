from django.conf.urls import url

from testapp import views

urlpatterns = [
    url(r'^index/', views.index),
]