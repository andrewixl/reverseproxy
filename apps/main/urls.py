from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addconfig$', views.addConfig),
    url(r'^update$', views.runUpdate),
    url(r'^remove/(?P<id>\d+)$', views.removeConfig),
    url(r'^addssl/(?P<id>\d+)$', views.addSSL),
    url(r'^renewssl/(?P<id>\d+)$', views.renewSSL),
]