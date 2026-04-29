from django import forms
from .models import Employe


class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['nom', 'email', 'poste', 'salaire']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'input input-bordered w-full',
                'placeholder': 'Ex: Jean Dupont'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input input-bordered w-full',
                'placeholder': 'email@exemple.com'
            }),
            'poste': forms.TextInput(attrs={
                'class': 'input input-bordered w-full',
                'placeholder': 'Ex: Développeur Backend'
            }),
            'salaire': forms.NumberInput(attrs={
                'class': 'input input-bordered w-full',
                'placeholder': 'Ex: 450000'
            }),
        }
