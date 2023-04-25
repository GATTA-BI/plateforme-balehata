from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('acceuil.urls') ),
    path('administ/', include('administrations.urls') ),
    path('prof/', include('professeurs.urls') ),
    path('institu/', include('instituteurs.urls') ),
    path('emarge/', include('emarge.urls') ),
    path('compte/', include('compte.urls') ),

]
