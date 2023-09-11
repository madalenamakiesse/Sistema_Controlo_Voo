from django import forms
from .models import *

class NacionalForm(forms.ModelForm):
    class Meta:
        model = Voo_Nacional
        fields = ('codigo', 'entrante', 'id_companhia_aerea', 'cidadeD', 'cidadeO', 'data', 'hora', 'id_aviao')

class AviaoForm(forms.ModelForm):
    class Meta:
        model = Aviao
        fields = ('registro', 'marca', 'modelo', 'numero_de_passageiros')

class CompanhiaForm(forms.ModelForm):
    class Meta:
        model = Companhia_Aerea
        fields = ('codigo', 'nome', 'numero_de_aeronaves', 'nacionalidade')