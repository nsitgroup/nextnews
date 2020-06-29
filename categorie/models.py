from django.db import models


# Create your models here.


class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    update = models.DateTimeField(auto_now_add=True)
    is_actif  = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

    @property
    def get_products(self):
        from news.models import News
        return News.objects.filter(categorie__nom=self.nom)