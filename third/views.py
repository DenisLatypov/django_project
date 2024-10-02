from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def tv(request):
    return HttpResponse('никто не любит смотреть телевизоры')

def cat(request):
    return HttpResponse('любите ваших кошечек')

def dog(request):
    return HttpResponse('Не забывайте кормить ваших собак')