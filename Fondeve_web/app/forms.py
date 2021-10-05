from django import forms
from .models import *

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

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Imagenes
        fields = ('title', 'image')