from django.shortcuts import render, redirect
from emarge.models import Emarge
from .forms import EmargeForm
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required(login_url='acces')
def emarge_home(request):
    emarge=Emarge.objects.all()
    context={'emarge':emarge}
    return render(request, 'emarge/emarge_home.html', context)

@login_required(login_url='acces')
def emarger(request):
    form=EmargeForm()
    if request.method=='POST':
        form=EmargeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/emarge/') 
    context={'form':form}
    return render(request, 'emarge/emarger.html', context)



