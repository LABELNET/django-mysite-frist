from django.conf.urls import url

from testForm.views import AddFoodView

urlpatterns = [
    url(r'^add', AddFoodView.as_view()),
]
