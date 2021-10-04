from django import forms
from .models import Contacto,Junta,Representante

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class JuntaForm(forms.ModelForm):

    class Meta:
        model = Junta
        fields = '__all__'

class RepresentanteForm(forms.ModelForm):

    class Meta:
        model = Representante
        fields = '__all__'