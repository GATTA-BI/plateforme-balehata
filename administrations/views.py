from django.shortcuts import render, redirect
from administrations.models import Administration
from .forms import AdministrationForm
from professeurs.models import Professeur
from django.contrib.auth.decorators import login_required 


# Create your views here.
@login_required(login_url='acces')
def admin_home(request):
    administra=Administration.objects.all()
    prof=Professeur.objects.all()
    context={'administra':administra, 'prof':prof}
    return render(request, 'administrations/admin_emarg.html', context)

@login_required(login_url='acces')
def ajouter(request):

    form=AdministrationForm()
    if request.method=='POST':
        form=AdministrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/administ/ajouter/') 
    contexte={'form':form}
    return render(request, 'administrations/ajouter.html', contexte)

@login_required(login_url='acces')
def modifier(request):
    modifie=Administration.objects.all()
    form=AdministrationForm(instance=modifie)
    if request.method=='POST':
        form=AdministrationForm(request.POST, instance=modifie)
        if form.is_valid():
            form.save()
            return redirect('/administ/') 
    contexte={'form':form}
    return render(request, 'administrations/ajouter.html', contexte)
