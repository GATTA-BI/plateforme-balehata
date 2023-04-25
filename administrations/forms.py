from django.forms import ModelForm
from .models import Administration

class AdministrationForm(ModelForm):
    class Meta:
        model=Administration
        fields='__all__'

