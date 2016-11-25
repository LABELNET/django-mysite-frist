from django.conf.urls import url

from .views import FoodList, FoodDetail

urlpatterns = [
    url(r'^index$', FoodList.as_view()),
    url(r'^detail/(?P<pk>[0-9]+)$', FoodDetail.as_view()),
]
