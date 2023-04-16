from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def govt(request):
    return render(request, 'detail.html')

@login_required(login_url='login')
def tech_education(request):
    return render(request, 'tech_knowledge.html')

@login_required(login_url='login')
def crop_education(request):
    return render(request, 'crop_knowledge.html')

@login_required(login_url='login')
def contact(request):
    return render(request, 'contact.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user=User.objects.create_user(username = uname,password = pass1)
            my_user.save()
            return redirect('login')

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

@login_required(login_url='login')
def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def CreatePost(request):
    if request.method=='POST':
        title_ =request.POST.get('title')
        content_ =request.POST.get('content')
        image_ =request.FILES['image']
        post = Post(user = request.user , title = title_ , content = content_ , image = image_)
        post.save()
        return redirect('home')
    return render (request,'create_post.html')

@login_required(login_url='login')
def AllPosts(request):
    if request.method=='GET':
        posts = Post.objects.all()
    return render (request,'all_posts.html', {"posts":posts})

@login_required(login_url='login')
def MyPosts(request):
    user = request.user
    posts = user.posts.all()
    return render(request, 'my_posts.html', {"posts":posts})