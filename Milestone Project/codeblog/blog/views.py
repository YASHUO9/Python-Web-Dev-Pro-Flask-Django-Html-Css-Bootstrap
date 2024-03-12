from django.shortcuts import render, HttpResponse

# Create your views here.
def blogpost(request,slug):
    return render(request, 'blog/blogpost.html')


def bloghome(request):
    return render(request, 'blog/bloghome.html')

