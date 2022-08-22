from django.urls import path
from . import views

app_name="Home_app"
urlpatterns=[
    path("",views.Home.as_view(),name="Home")
]
