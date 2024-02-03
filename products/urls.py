from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posters, name='posters' ),
    path('<int:poster_id>/', views.poster_detail, name='poster_detail' ),
    path('add/', views.add_poster, name='add_poster' ),
]
