from django.conf.urls import url

from .views import FoodList

urlpatterns = [
    url(r'^index$', FoodList.as_view())
]
