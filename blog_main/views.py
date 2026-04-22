from django.shortcuts import render,redirect
from blog_app.models import Blog,Category
from assignments.models import About
from .forms import RegistrationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth



def home(request):
    
    # categories = Category.objects.all()
    # print(categories)
    
    featured_posts = Blog.objects.filter(is_featured = True,status='Published')
    # print(featured_posts)
    
    posts = Blog.objects.filter(is_featured=False, status='Published').order_by('-updated_at')
    # print(posts)
    
    #about us fetch    - get will fetch only 1 single data and try will only work with get
    try:
        about = About.objects.get()
    except:
        about = None
    
    context = {
        # 'categories':categories,
        'featured_posts':featured_posts,
        'posts':posts,
        'about':about,
    }
    return render(request,'home.html',context)


def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            current_user = form.save(commit=False)
            form.save()
            send_mail("Welcome to Django Blogs","Congratulations on creating an account on Django Blogs app - Sidharth Jain.",settings.DEFAULT_FROM_EMAIL,[current_user.email])
            return redirect('login')
        
    else:
        form = RegistrationForm()
        
    context = {
        'form':form,
    }
    return render(request,'register.html',context)

def login(request):
    
    if request.method=='POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    
    context = {
        'form':form,
    }
    return render(request,'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('home')