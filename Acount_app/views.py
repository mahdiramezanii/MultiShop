from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from  Acount_app.models import User,Otc
from random import randint
from Acount_app.forms import LoginForm,RegisterForm,OtcCodeForms
from django.views.generic.base import View
from django.urls import reverse
from django.utils.crypto import get_random_string
import ghasedakpack
from django.utils import timezone

SMS = ghasedakpack.Ghasedak("1dd33ef4c344cdaffb310154439cb9bbfe4a8301ad0bfa894117acc4b190164a")

class LoginView(View):
    form=LoginForm()
    def post(self,request):
        form=LoginForm(data=request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            username=cd.get("username")
            password=cd.get("password")
            user=authenticate(username=username,password=password)
            login(request,user,backend="Acount_app.authentication.EmailAuthBackend")
            return redirect("/")

        return render(request,"Acount_app/login.html",{"form":form})

    def get(self,request):
        form = LoginForm()

        return render(request, "Acount_app/login.html",{"form":form})

class RegisterLoginView(View):

    def post(self,request):
        form=RegisterForm(data=request.POST)

        if form.is_valid():
            phone=form.cleaned_data.get("phone")
            random_number=randint(1000,2000)
            print(random_number)
            token=get_random_string(length=30)
            #SMS.verification({'receptor': phone,'type': '1','template': 'MultyShop','param1': random_number})
            Otc.objects.create(phone=phone,code=random_number,token=token)

            return redirect(reverse("Acount_app:otc")+f"?token={token}")


        return render(request,"Acount_app/register.html",{"form":form})



    def get(self,request):
        form=RegisterForm()
        return render(request,"Acount_app/register.html",{"form":form})


class OtcCodeView(View):

    def post(self,request):
        form=OtcCodeForms(data=request.POST)

        if form.is_valid():
            code=form.cleaned_data.get("code")
            token=request.GET.get("token")

            if Otc.objects.filter(code=code,token=token).exists():
                otc=Otc.objects.get(token=token)

                if otc.is_expiration_date():

                    user,is_exisit=User.objects.get_or_create(phone=otc.phone)
                    login(request,user,backend="Acount_app.authentication.EmailAuthBackend")
                    otc.delete()
                    return redirect("Home_app:Home")
                else:
                    form.add_error("code", "code is current")
            else:
                form.add_error("code","code is current")

        return render(request,"Acount_app/otc_code.html",{"form":form})

    def get(self,request):
        form=OtcCodeForms()
        return render(request,"Acount_app/otc_code.html",{"form":form})



class LogOutView(View):

    def get(self,request):

        logout(request)
        return redirect("Home_app:Home")

# def register_user(request):
#     form=RegisterForm()
#
#     if request.method=="POST":
#         form=RegisterForm(data=request.POST)
#
#         if form.is_valid():
#             cd=form.cleaned_data
#             username=cd.get("username")
#             email=cd.get("email")
#             password1=cd.get("password1")
#             user=User.objects.create(phone=username,email=email,password=password1)
#             user.set_password(password1)
#             user.is_active=False
#             user.save()
#             return redirect("Acount_app:login")
#
#         return render(request,"Acount_app/register.html",{"form":form})
#
#     return render(request,"Acount_app/register.html",{"form":form})




