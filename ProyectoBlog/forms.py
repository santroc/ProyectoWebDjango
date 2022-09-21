from email import contentmanager
from socket import fromshare
from turtle import title
from django import forms




class PostFormulario(forms.Form):

    title = forms.CharField()
    content = forms.CharField()
    created_on = forms.DateField()