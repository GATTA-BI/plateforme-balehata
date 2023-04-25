
from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_home),
    path('ajouter/', views.ajouter, name="ajouter"),
    path('modifier/', views.modifier, name="modifier"),
]

