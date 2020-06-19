from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    lastname = forms.CharField(label='Nom', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    firstname = forms.CharField(label='Prénom', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    email = forms.EmailField(label='Adresse email', widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)
    subject = forms.CharField(label='Sujet', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-control'}), required=True)
    
    class Meta:
        model=Contact #or whatever object
        fields = ['lastname', 'firstname', 'email', 'subject', 'message']


class TargetForm(forms.ModelForm):
    target = forms.CharField(label='A qui voulez-vous contacter ?')
    
    class Meta:
        model=Contact #or whatever object
        fields = ['target']