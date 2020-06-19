from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

TARGET = (
    ('SC', 'Service commercial'),
    ('ST', 'Webmaster'),
    ('DG', 'Direction'),
    ('C', 'Candidature'),
    ('X', 'Default')
)
# Create your models here.
class Contact(models.Model):
    lastname = models.CharField(max_length=200, blank='true', null=True)
    firstname = models.CharField(max_length=200, blank='true', null=True)
    message = RichTextField()
    subject = models.CharField(max_length=200, default='Contact')
    email = models.CharField(max_length=200)
    date_modif = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, null=True)
    is_treat = models.BooleanField(default=False, null=True)
    target = models.CharField(choices=TARGET, max_length=2, default='X')

    def __str__(self):
        return self.email
