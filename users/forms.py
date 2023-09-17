from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from django.utils.timezone import now
from .models import User




class UserLoginForm(AuthenticationForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': '...', 'placeholder': 'Введите имя'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={
        'class': '...', 'placeholder': 'Введите фамилию'}))
    studcode = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': '...', 'placeholder': 'Введите номер зачетной книжки'}))

    class Meta:
        model = User
        fields = ('username', 'lastname', 'studcode')
