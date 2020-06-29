from django.http import HttpResponse
from django.shortcuts import render, redirect

from categorie.models import Categorie
from news.models import News
from django.db.models import Count

def homepage(request):


    categories = Categorie.objects.annotate(num_news=Count('news'))
    cats = Categorie.objects.all()
    news = News.objects.all()
    societes = News.objects.all()

    return render(request, "home.html", locals())

def aboutpage(request):
    return render(request, "about.html")

def cgupage(request):
    return render(request, "cgu.html")