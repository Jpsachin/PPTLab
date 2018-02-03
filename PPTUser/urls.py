from django.conf.urls import url
from . import templates, views 
urlpatterns = [
    url(r'^$', views.Index, name='Index'),
]