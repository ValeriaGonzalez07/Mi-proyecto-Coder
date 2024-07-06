from django import forms
from .models import MainModel

class MainModelForm(forms.ModelForm):
    class Meta:
        model = MainModel
        fields = ['Bienvenido a mi proyecto', 'Este es mi primer proyecto utilizando Django', 'Gonzalez Valeria', 'image']
