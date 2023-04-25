
from django.urls import path
from . import views

urlpatterns = [
    path('', views.emarge_home),
    path('emarger/', views.emarger, name='emarger'),
    
]

