from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


def login_form(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        current_user = auth.authenticate(request, username=username, password=password)
               
        if current_user is not None:   # if login success
            auth.login(request, current_user)
            return redirect("home-page")  # redirect user to 'home page'
        
        else:
            messages.info(request, "User does not exist!")
            return redirect('login-form')  # redirect user to 'login page'
    return render(request, "loginForm/login-page.html", {})


def register_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pw1 = request.POST['password1']
        pw2 = request.POST['password2']
        
        if pw1 == pw2:
            
            # check if "username" already existed
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already existed!")
                return redirect("register-form")
            else:
                # create new User
                new_user = User.objects.create_user(username=username, email=email, password=pw1)
                new_user.save()
                
                # after 'register', redirect user to 'home page'
                current_user = auth.authenticate(request, username=username, password=pw1)
                auth.login(request, current_user)
                return redirect("home-page")
            
    return render(request, "loginForm/register-page.html", {})


def logout_form(request):
    auth.logout(request)
    return redirect("login-form")