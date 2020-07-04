from django import forms
from django.contrib.auth.models import User

from slippery import settings


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, max_length=255)
    install_key = forms.CharField(label='Install Key', max_length=255)

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )

    def clean(self):
        cleaned_data = super().clean()
        raise forms.ValidationError('Invalid install key.')
