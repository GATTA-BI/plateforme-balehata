from django.shortcuts import render
from instituteurs.models import Instituteur


# Create your views here.
def home_institu(request):
    insti=Instituteur.objects.all()
    context={'insti':insti}
    return render(request, 'instituteurs/institu_emarg.html', context)