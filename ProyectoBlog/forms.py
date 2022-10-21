from .models import *
from email import contentmanager
from tkinter import Widget
from turtle import title
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from UserManagement.models import PerfilUsuario

class PostFormulario(forms.Form):

    title = forms.CharField()
    content = forms.CharField()
    created_on = forms.DateField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        
# class UserRegisterForm(UserCreationForm):

#     email = forms.EmailField()
#     password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)
#     password2 = forms.CharField(label = 'Repetir contraseña', widget = forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#         help_texts = {k:"" for k in fields}

# class UserEditForm(UserChangeForm):
#     username = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Username'}))
#     email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder': 'Email'}))
#     first_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'First name'}))
#     last_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Last name'}))
#     password= forms.CharField(widget= forms.PasswordInput(attrs={'placeholder': 'Password'}))

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name', 'password']
#         help_texts = {k: "" for k in fields}

# class UserProfileEditForm(forms.ModelForm):
#     description = forms.CharField(widget= forms.Textarea(attrs={'placeholder': 'Description'}))
#     web_link = forms.URLField(widget= forms.URLInput(attrs={'placeholder': 'URL'}))

#     class Meta:
#         model = PerfilUsuario
#         fields = ['description', 'web_link']
#         help_texts = {k: "" for k in fields}


# class ChangePasswordForm(PasswordChangeForm):
#     old_password = forms.CharField(label="", widget= forms.PasswordInput(attrs={'placeholder': "Old Password"}))
#     new_password1 = forms.CharField(label="",widget= forms.PasswordInput(attrs={'placeholder': "New password"}))
#     new_password2 = forms.CharField(label="",widget= forms.PasswordInput(attrs={'placeholder': "Confirm new password"}))

#     class Meta:
#         model = User
#         fields = ['old_password', 'new_password1', 'new_password2']
#         help_texts = {k:"" for k in fields}

# class AvatarFormulario(forms.Form):
#     avatar = forms.ImageField()