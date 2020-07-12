from django import forms

from slippery.contrib.databases.models import Database


class DatabaseForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(widget=forms.PasswordInput, label="Password Again")

    # TODO: Add password validation.

    class Meta:
        model = Database
        fields = '__all__'
