from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    print('++++++++++++++++++++++++++++++++++++homepage')
    return render(request, "news/case.html")

def case_follow(request, case_id):
    print(case_id)
    print('++++++++++++++++++++++++++++++++++++case_follow')
    return render(request, "news/case.html")

def news_details(request):
    print('++++++++++++++++++++++++++++++++++++news_details')
    return render(request, "news/news.html")