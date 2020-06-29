from django.db import models
from ckeditor.fields import RichTextField

from categorie.models import Categorie
from nextnews.settings import base


STATUS = (
    ('D', 'Draft'),
    ('P', 'Publish'),
    ('R', 'Remove'),
    ('X', 'Default')
)


class Case(models.Model):
    title = models.CharField(max_length=200)
    inProgress = models.BooleanField(default=False)
    linkedCase = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class News(models.Model):
    title = models.CharField(max_length=500)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastModifiedDate = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(base.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    resume = models.TextField(null=True, blank=True)
    post = models.TextField(null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=2, default='X')
    image = models.ImageField()
    nbView = models.IntegerField(default=0)
    nbLike = models.IntegerField(default=0)
    nbUnlike = models.IntegerField(default=0)
    nbComment = models.IntegerField(default=0)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, blank='true', null=True)
    step = models.IntegerField(default=0)
    link = models.CharField(max_length=200, blank='true', null=True)
    
    def __str__(self):
        return self.title



    """
    def get_absolute_url(self):
            return reverse("product:product", kwargs={
                'slug': self.slug
            })"""
    
class Subcription(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    customer = models.ForeignKey(base.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_inProgress = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title