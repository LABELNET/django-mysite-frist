from django.conf.urls import url

from store import views

urlpatterns = [
    url(r'^list$', views.select_store_list),
    url(r'^add$', views.add_store_info),
    url(r'^delete/(?P<pk>[0-9]+)$', views.delete_store_info),
]
