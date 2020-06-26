from django.contrib import admin
from django.conf.urls import url
from . import views
from django.urls import path



app_name = 'news'

urlpatterns = [
    path('', views.homepage , name='case'),
    path('case/<int:case_id>/', views.case_follow, name='followCase'),
    path('news/<str:cat_id>/', views.category_news, name='categoryNews'),

    path('news', views.news_list, name='indexNews'),
    path('create/', views.news_create, name='createNews'),
    path('<int:news_id>/', views.news_detail, name='detailNews'),
    #path('view/<int:news_id>/', views.news_view, name='viewNews'),
    path('edit/<int:news_id>/', views.news_edit, name='editNews'),
    path('delete/<int:news_id>/', views.news_delete, name='deleteNews'),



    path('case', views.case_list, name='indexCase'),
    path('case/create/', views.case_create, name='createCase'),
    path('case/show/<int:case_id>/', views.case_detail, name='detailCase'),
    #path('view/<int:case_id>/', views.case_view, name='viewCase'),
    path('case/edit/<int:case_id>/', views.case_edit, name='editCase'),
    path('case/delete/<int:case_id>/', views.case_delete, name='deleteCase'),

]
