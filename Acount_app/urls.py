from django.urls import path
from . import views

app_name="Acount_app"
urlpatterns=[
    path("login/",views.login_user,name="login"),
    path("register/",views.register_user,name="register")
]
