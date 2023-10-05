from django.forms import ModelForm
from django import forms
from finecap.models import Stand

class StandForm(ModelForm):

    class Meta:
        model= Stand
        fields='__all__'

    localizacao=forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control ",
            "placeholder": "Valor da localização",
        })
    )

  
    valor = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control money",
            "placeholder": "Valor do stand",
        })
    )

    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        return valor.replace(",", ".")
