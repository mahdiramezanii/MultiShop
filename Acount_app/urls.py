from django.urls import path
from . import views

app_name="Acount_app"
urlpatterns=[
    path("login/",views.LoginView.as_view(),name="login"),
    path("register/",views.RegisterLoginView.as_view(),name="register"),
    path("otc",views.OtcCodeView.as_view(),name="otc"),
    path("logout",views.LogOutView.as_view(),name="logout"),
]
