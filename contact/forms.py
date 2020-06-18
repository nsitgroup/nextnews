from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact #or whatever object
        fields = ['Nom', 'Prenom', 'Email', 'Message']
