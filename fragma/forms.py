from django import forms
from .models import cadastro



class CadastroForm(forms.ModelForm):
    class Meta:
        model = cadastro
        fields = ['nome', 'idade', 'chave', 'doar']
       