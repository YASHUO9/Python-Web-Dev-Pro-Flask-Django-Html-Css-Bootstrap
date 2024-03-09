from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
import random


# Create your views here.
def home(request):
    return render(request, 'home.html')


def passgen(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get('digit'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+{}:">?"'))    
    length = int(request.GET.get('length',10))
    password = ''
    for i in range(length):
        password += random.choice(characters)
        
    
    return render(request, 'password.html',{'password': password})
    