from django.contrib import admin
from django.conf.urls import url
from . import views
from django.urls import path



app_name = 'news'

urlpatterns = [
    path('', views.homepage , name='case'),
    path('case/<int:case_id>/', views.case_follow, name='followCase'),
    path('news/<str:cat_id>/', views.category_news, name='categoryNews')

]
