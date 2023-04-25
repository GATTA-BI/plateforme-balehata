from django.shortcuts import render

# Create your views here.
def acceuil_home(request):
    return render(request, 'acceuil/acceuil_menu.html')
