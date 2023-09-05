from django.shortcuts import render
from .models import *
# Create your views here.

def index (request):
    return render(request, 'index.html')

def index(request):
    all_banners = Banner.objects.all()
    all_disciplines = Discipline.objects.all()
    return render(request,'index.html',{"banner": all_banners, "discipline": all_disciplines})