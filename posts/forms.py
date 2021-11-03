from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from posts.models import *


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                             'aria-label': 'Sizing example input',
                                                                             'aria-describedby': 'inputGroup-sizing-default'}))
    slug = forms.SlugField(label='Slug', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                       'aria-label': 'Sizing example input',
                                                                       'aria-describedby': 'inputGroup-sizing-default'}))
    content = forms.CharField(label='Содержание', widget=forms.Textarea(attrs={'class': 'form-control textarea-post',
                                                                               'style': 'height: 125px',
                                                                               'placeholder': 'Leave a comment here'}))

    class Meta:
        model = Posts
        fields = ['title', 'slug', 'content']


class ProfileForm(forms.ModelForm):
    role = forms.ModelChoiceField(queryset=Role.objects.all(), label='Роль', initial=0,
                                  widget=forms.Select(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Profile
        fields = ['role']
