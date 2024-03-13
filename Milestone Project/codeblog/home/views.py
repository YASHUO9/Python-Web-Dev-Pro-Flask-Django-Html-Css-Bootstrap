from django.shortcuts import render,HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post
# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def contact(request):
    messages.success(request, 'Welcome to the contact page')
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        content = request.POST['content']
        
        if len(name)<2 or len(phone)<10 or len(email)<3 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, phone=phone, email=email, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
        
        
        
        
        print(name, phone, email, content)
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html') 


def search(request):
    allposts = Post.objects.filter(title__icontains=request.GET['query'])
    params = {'allposts': allposts}
    return render(request, 'home/search.html', params)
    
   
    