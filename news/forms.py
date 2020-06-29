from django import forms
from . import models

class CreateCase(forms.ModelForm):
    class Meta:
        model = models.Case
        fields = ['title', 'inProgress']


class CreateNews(forms.ModelForm):
    class Meta:
        model = models.News
        fields = ['title', 'resume', 'post', 'categorie', 'image', 'case']