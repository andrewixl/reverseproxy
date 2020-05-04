from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addconfig$', views.addConfig),
    url(r'^remove/(?P<id>\d+)$', views.removeConfig),
]