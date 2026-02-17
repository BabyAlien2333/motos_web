from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Correo electrónico"
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            "username": "Usuario",
            "password1": "Contraseña",
            "password2": "Confirmar contraseña",
        }
        help_texts = {
            "username": "",
            "password1": "",
            "password2": "",
        }
