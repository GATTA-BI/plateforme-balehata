from django.shortcuts import render
from professeurs.models import Professeur

# Create your views here.
def home_prof(request):

    prof=Professeur.objects.all()
    context={'prof':prof}
    return render(request, 'professeurs/prof_emarg.html', context)