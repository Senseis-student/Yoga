from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('program', views.view_program, name='view_program'),
    path('price', views.price_list, name= 'price_list')
]