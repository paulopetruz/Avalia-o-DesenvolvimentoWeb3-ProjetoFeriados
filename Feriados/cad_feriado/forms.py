from django.forms import ModelForm

from API.models import FeriadoModel


class FeriadoForm(ModelForm):
    class Meta:
        model = FeriadoModel
        fields = ['nome', 'data']