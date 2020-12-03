from django import forms
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username     = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    "placeholder": "Matricula"
                }
            )
        )
    password     = forms.CharField(
        widget=forms.PasswordInput(
            attrs={ 
                    "placeholder": "Senha"
                }
            )
        )

class RegisterForm(forms.Form):
    CHOICES = (
        (0, 'Professor(a)'),
        (1, 'Caest'),
    )
    username     = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    "class": "inpt", 
                    "placeholder": "               Nome Completo"
                }
            )
        )
    matricula = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    "class": "inpt",  
                    "placeholder": "                      Matricula"
                }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={ 
                    "class": "inpt", 
                    "placeholder": "                         Senha"
                }
            )
        )
    radio_choices = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                "class": "op",
            }
        ),
        choices=CHOICES,
    )
