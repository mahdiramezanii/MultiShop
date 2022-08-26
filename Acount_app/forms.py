from django import forms
from Acount_app.models import User
from django.contrib.auth import authenticate
from django.forms import ValidationError
from django.core import validators




class LoginForm(forms.Form):
    username=forms.CharField(validators=[validators.MaxLengthValidator(11)],widget=forms.TextInput(attrs={"class":"input100","placeholder":"Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"input100","placeholder":"Password"}))

    def clean(self):
        cd=self.cleaned_data
        username=cd.get("username")
        password=cd.get("password")
        user=authenticate(username=username,password=password)
        if user is None:
            raise ValidationError("username or password is current")

        return super(LoginForm,self).clean()

class RegisterForm(forms.Form):
    username=forms.CharField(validators=[validators.MaxLengthValidator(11),validators.MinLengthValidator(10)],
                             widget=forms.TextInput(attrs={"class":"input100","placeholder":"Phone Number"})
                             )
    email=forms.EmailField(widget=forms.TextInput(attrs={
        "class":"email-input input100","placeholder":"Email"
    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"input100",
        "placeholder":"Password1"
    }))

    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"input100",
        "placeholder":"Password2"
    }))


    def clean(self):
        cd=self.cleaned_data

        password1=cd.get("password1")
        password2=cd.get("password2")

        if password1 != password2:
            raise ValidationError("password1 and password2 is not same!!!")

        return super(RegisterForm, self).clean()

    def clean_username(self):

        cd=self.cleaned_data
        phone=cd.get("username")

        user=User.objects.filter(phone=phone)

        if user.exists():
            raise ValidationError("phone number is already exist!!!")

        return cd.get("username")

    def clean_email(self):
        cd=self.cleaned_data
        email=cd.get("email")
        user=User.objects.filter(email=email)

        if user.exists():
            raise ValidationError("email is already exists!!!")

        return cd.get("email")




