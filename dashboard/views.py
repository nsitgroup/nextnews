from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.db.models import Count
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required(login_url='/account/login/')
def dashboard(request):
    classe_active=1
    return render(request, "dashboard/dashboard.html", locals())