from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# Create your models here.
class Contact(models.Model):
    Nom = models.CharField(max_length=200, blank='true', null=True)
    Prenom = models.CharField(max_length=200, blank='true', null=True)
    Message = RichTextField()
    Sujet = models.CharField(max_length=200, default='Contact')
    Email = models.CharField(max_length=200)
    Date_modification = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, null=True)
    is_treat = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.Email
