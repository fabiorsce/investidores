from django.forms import ModelForm
from investidores.models import Desejo

class DesejoForm(ModelForm):
    class Meta:
        model = Desejo