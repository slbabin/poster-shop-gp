from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home' ),
    path('terms/', views.terms, name='terms' ),
    path('about/', views.about, name='about' ),
    path('return/', views.returnpolicy, name='return' ),
    path('contact/', views.contact, name='contact' ),
    path('newsletters/', views.newsletters, name='newsletters' ),
    
]
