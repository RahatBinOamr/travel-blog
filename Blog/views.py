from django.shortcuts import render, redirect
from .models import Blog, Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import ContactForm
# Create your views here.


def HomePage(request):
    blogs = Blog.objects.all().order_by('-blog_title')

    context = {
        'blogs': blogs
    }
    return render(request, 'index.html', context)


def blog_details(request, slug):
    blog = Blog.objects.get(blog_slug=slug)
    blogs = Blog.objects.all().order_by('blog_title')

    context = {
        'blog': blog,
        'blogs': blogs,

    }
    return render(request, 'blog_detail.html', context)


def Register(request):
    m = ""
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        print(name, email, pass1, pass2)
        if (pass1 != pass2):
            m = "wrong password!!!"
        else:
            signUp = User.objects.create_user(
                username=name,
                email=email,
                password=pass1
            )
            signUp.save()
            return redirect('login')

    return render(request, 'register.html', {m: m})


def Login(request):
    m = ""
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        loginUser = authenticate(
            request,
            username=name,
            password=password
        )
        if loginUser is not None:
            login(request, loginUser)
            return redirect('/')
        else:
            m = "something went wrong"
    return render(request, 'login.html', {'m': m})


def LogOut(request):
    logout(request)
    return redirect('login')


def Contact(request):
    forms = ContactForm()
    if request.method == "POST":
        forms = ContactForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    context = {'forms': forms}
    return render(request, 'contact.html', context)
