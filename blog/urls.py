from django.conf.urls import url
from . import views
from django.conf.urls import include

urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
        ]
