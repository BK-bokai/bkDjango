# users/forms.py
from django import forms
from django.forms import ModelForm
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class LoginForm(ModelForm):
    username = forms.CharField(label="使用者名稱", error_messages={'required': '請勿為空'},
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '使用者名稱'}))
    password = forms.CharField(min_length=6, label="密碼", error_messages={'min_length': '請勿小於6碼'},
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密碼'}))
    class Meta:
        model = User
        fields = ("username", "password")
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control', 'placeholder': '使用者名稱'}),
            "password": forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密碼'}),
        }
