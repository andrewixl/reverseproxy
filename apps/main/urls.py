from . import views
from django.conf.urls import url
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addconfig$', views.addConfig),
    url(r'^update$', views.runUpdate),
    url(r'^settings$', views.settings),
    url(r'^addauth$', views.addAuth),
    url(r'^disableauth$', views.disableAuth),
    url(r'^login$', views.loginAuth),
    url(r'^loginval$', views.loginVal),
    url(r'^logout$', views.logout),
    url(r'^remove/(?P<id>\d+)$', views.removeConfig),
    url(r'^addssl/(?P<id>\d+)$', views.addSSL),
    url(r'^renewssl/(?P<id>\d+)$', views.renewSSL),
    url(r'^imports$', views.imports),
    url(r'^exportconfig$', views.exportConfig),
]