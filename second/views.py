from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def box(request):
    return HttpResponse('коробочка')

def car(request):
    return HttpResponse('здесь могла быть ваша машина')

def wheel(request):
    return HttpResponse('Покупайте колеса на авто заранее')
