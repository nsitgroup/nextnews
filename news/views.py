from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from news.models import News, Case
from django.contrib import messages
from . import forms
from .forms import CreateNews, CreateCase
from django.http import Http404

CATEGORY = (
    
)

def homepage(request):
    print('++++++++++++++++++++++++++++++++++++homepage')
    return render(request, "news/case.html")

def case_follow(request, case_id):
    print(case_id)
    print('++++++++++++++++++++++++++++++++++++case_follow')
    return render(request, "news/case.html")

def category_news(request, cat_id):
    print('++++++++++++++++++++++++++++++++++++cat_id : ' + cat_id)
    # get news here by cat_id
    return render(request, "news/news.html")



def news_list(request):
    classe_active = 'news'
    news = News.objects.all()
    return render(request, "news/news_list.html", locals())

def news_create(request):
    classe_active = 'news'
    if request.method == 'POST':
        form = CreateNews(request.POST, request.FILES)
        if form.is_valid():
            # save article to DB # DEBUG: # TODO:

            messages.success(request, "L'information a été ajoutée avec succès !")
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('news:indexNews')
    else:
        form = CreateNews()
    return render(request, 'news/news_create.html', {'form': form, 'classe_active': classe_active})


def news_detail(request, news_id):
    classe_active = 'news'
    try:
        news = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        raise Http404("La news n'existe pas")
    return render(request, 'news/news_detail.html', {'news': news, 'classe_active': classe_active})


def news_view(request, news_id):
    classe_active=3
    news = News.objects.all().exclude(pk=news_id)[:5]
    try:
        news = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        raise Http404("La news n'existe pas")
    return render(request, 'news/view_news.html', locals())


def news_edit(request, news_id):
    classe_active = 'news'
    post = get_object_or_404(News, pk=news_id)
    if request.method == 'POST':
        form = CreateNews(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # save news to DB # DEBUG: # TODO:
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, "L'information a été mofifiée avec succès !")
            return redirect('news:indexNews')
    else:
        form = CreateNews(instance=post)

    return render(request, 'news/news_create.html', {'form': form, 'classe_active': classe_active})


def news_delete(request, news_id):
    news= News.objects.filter(pk=news_id)
    news.delete()
    messages.success(request, "L'information a été supprimée avec succès !")

    return redirect('news:indexNews')


def news(request):
    classe_active= 'news'
    news = News.objects.all()
    return render(request, "news/news.html", locals())


def case_list(request):
    classe_active = 'case'
    cases = Case.objects.all()
    return render(request, "case/case_list.html", locals())

def case_create(request):
    classe_active = 'case'
    if request.method == 'POST':
        form = CreateCase(request.POST, request.FILES)
        if form.is_valid():
            # save article to DB # DEBUG: # TODO:

            messages.success(request, "L'information a été ajoutée avec succès !")
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('news:indexCase')
    else:
        form = CreateCase()
    return render(request, 'case/case_create.html', {'form': form, 'classe_active': classe_active})


def case_detail(request, case_id):
    classe_active = 'case'
    try:
        case = Case.objects.get(pk=case_id)
    except Case.DoesNotExist:
        raise Http404("La case n'existe pas")
    return render(request, 'case/case_detail.html', {'case': case, 'classe_active': classe_active})


def case_view(request, case_id):
    classe_active=3
    case = Case.objects.all().exclude(pk=case_id)[:5]
    try:
        case = Case.objects.get(pk=case_id)
    except Case.DoesNotExist:
        raise Http404("La case n'existe pas")
    return render(request, 'case/view_case.html', locals())


def case_edit(request, case_id):
    classe_active = 'case'
    post = get_object_or_404(Case, pk=case_id)
    if request.method == 'POST':
        form = CreateCase(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # save case to DB # DEBUG: # TODO:
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, "L'information a été mofifiée avec succès !")
            return redirect('news:indexCase')
    else:
        form = CreateCase(instance=post)

    return render(request, 'case/case_create.html', {'form': form, 'classe_active': classe_active})


def case_delete(request, case_id):
    case= Case.objects.filter(pk=case_id)
    case.delete()
    messages.success(request, "L'information a été supprimée avec succès !")

    return redirect('news:indexCase')