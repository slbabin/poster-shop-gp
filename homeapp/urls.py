from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home' ),
    path('terms/', views.terms, name='terms' ),
    path('about/', views.about, name='about' ),
    path('privacy/', views.privacypolicy, name='privacy' ),
    path('contact/', views.contact, name='contact' ),
    path('shipping/', views.shipping, name='shipping' ),
    path('faq/', views.faq, name='faq' ),
    path('newsletters/', views.newsletters, name='newsletters' ),
    
]
