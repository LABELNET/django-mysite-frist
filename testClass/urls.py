from django.conf.urls import url

from .views import FoodList, FoodDetail, FoodListDef, FoodListQuery

urlpatterns = [
    url(r'^index$', FoodList.as_view()),
    url(r'^indexdef$', FoodListDef.as_view()),
    url(r'^indexquery$', FoodListQuery.as_view()),
    url(r'^detail/(?P<pk>[0-9]+)$', FoodDetail.as_view()),
]
