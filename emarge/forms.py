from django.forms import ModelForm
from .models import Emarge

class EmargeForm(ModelForm):
    class Meta:
        model=Emarge
        fields='__all__'

