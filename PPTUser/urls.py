from django.conf.urls import url
from . import templates, views

urlpatterns =[
	url(r'^$', views.Index, name='Index'),
    #url(r'^signup/', views.SignUpFormView.as_view(), name='signup'),
    url(r'^login/', views.login, name='login'),
    url(r'^about/', views.about, name='about'),
    url(r'^events/', views.events, name='events'),
    url(r'^bestdeals/', views.bestdeals, name='bestdeals'),
    url(r'^services/', views.services, name='services'),
    url(r'^specialoffers/', views.specialoffers, name='specialoffers'),
    url(r'^mail/', views.mail, name='mail'),
    url(r'^economics/', views.economics, name='economics'),
    url(r'^products/', views.products, name='products'),
	url(r'^sungle/', views.single, name='single'),
	url(r'^faqs/', views.faqs, name='faqs'),
	url(r'^privacy/', views.privacy, name='privacy'),
]