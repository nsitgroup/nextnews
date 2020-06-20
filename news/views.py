from django.shortcuts import render
from django.http import HttpResponse

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