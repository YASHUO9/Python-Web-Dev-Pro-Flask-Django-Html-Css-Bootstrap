from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")


def blog(request):
    return HttpResponse("This is the blog page.")   

