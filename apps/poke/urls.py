from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^pokes$', views.pokes),
    url(r'^create_poke/(?P<user_id>\d+)$', views.create_poke),
] 
