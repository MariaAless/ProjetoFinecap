from django.forms import ModelForm
from django import forms
from finecap.models import Stand

class StandForm(ModelForm):

    class Meta:
        model= Stand
        fields='__all__'

        widgets = {
            'localizacao' : forms.TextInput(attrs={'class': 'form-control'}),
            'valor' : forms.TextInput(attrs={'class': 'form-control' }),
            
        }