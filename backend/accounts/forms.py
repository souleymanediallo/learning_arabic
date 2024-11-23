from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'user_type', 'password1', 'password2']
        labels = {
            "first_name": "Prénom",
            "last_name": "Nom",
            "email": "Adresse Email",
            "user_type": "Vous êtes ?",
            "password1": "Mot de passe",
            "password2": "Confirmer le mot de passe",
        }
        widgets = {
        "user_type": forms.RadioSelect(),
        }

    placeholders = {
        'user_type': 'Vous êtes ?',
        'email': 'Adresse email',
        'first_name': 'Saisir votre prénom',
        'last_name': 'Saisir votre nom',
        'password1': 'Mot de passe, 8 caractères minimum',
        'password2': 'Confirmez votre mot de passe',
    }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': self.placeholders[name]})

        self.fields['user_type'].widget.attrs.update({
            'class': 'form-check-input'
        })


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'user_type']
        labels = {
            "first_name": "Prénom",
            "last_name": "Nom",
            "email": "Adresse Email",
            "user_type": "Vous êtes ?",
        }
        widgets = {
            "user_type": forms.RadioSelect(),

        }

    def __init__(self, *args, **kwargs):
        super(CustomUserUpdateForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['user_type'].widget.attrs.update({
            'class': 'form-check-input'
        })


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'description']
        labels = {
            "image": "Photo de profil",
            "description": "Description de votre profile",
        }

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['image'].widget.attrs.update({
            'class': 'form-control-file'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control'
        })