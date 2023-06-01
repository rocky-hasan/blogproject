from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from blog.forms import Signup, Login, PostForm ,ContactForm
from blog.models import Post
from django.contrib.auth.models import Group


# Create your views here.
# Home
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


# About
def about(request):
    return render(request, 'about.html')


# Contact
def contact(request):
    if request.method == 'POST':
        fm = ContactForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = ContactForm()
    return render(request, 'contact.html', {'form': fm})


# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps=user.groups.all()
        return render(request, 'dashboard.html', {'post': posts,'full_name': full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')


# Signup
def user_signup(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            messages.success(request, 'Signup successfully !')
            user=form.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form = Signup()
    return render(request, 'signup.html', {'form': form})


# Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = Login(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'logged in successfully !')
                    return HttpResponseRedirect('/dashboard/')

        else:
            form = Login()
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')


# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')



 # Add post
def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PostForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Add post successfully !')
                title=form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst=Post(title=title, desc=desc)
                pst.save()
                form = PostForm()

        else:
            form=PostForm()
        return render(request, 'addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
#UPDATE POST
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                form=PostForm()
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)
        return render(request, 'update.html',{'form': form})
    else:
        return HttpResponseRedirect('/login/')

# Delete post
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')