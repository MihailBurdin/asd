from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def tovar(request):
    return HttpResponse(request,'tovar.html')
