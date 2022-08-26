from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from  Acount_app.models import User
from Acount_app.forms import LoginForm,RegisterForm

def login_user(request):
    form=LoginForm()


    if request.method=="POST":
        form=LoginForm(data=request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            username=cd.get("username")
            password=cd.get("password")
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect("/")

        return render(request,"Acount_app/login.html",{"form":form})

    return render(request, "Acount_app/login.html",{"form":form})


def register_user(request):
    form=RegisterForm()

    if request.method=="POST":
        form=RegisterForm(data=request.POST)

        if form.is_valid():
            cd=form.cleaned_data
            username=cd.get("username")
            email=cd.get("email")
            password1=cd.get("password1")
            user=User.objects.create(phone=username,email=email,password=password1)
            user.set_password(password1)
            user.is_active=False
            user.save()
            return redirect("Acount_app:login")

        return render(request,"Acount_app/register.html",{"form":form})

    return render(request,"Acount_app/register.html",{"form":form})




