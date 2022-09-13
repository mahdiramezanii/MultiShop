from django.urls import path
from . import views

app_name="Product_app"
urlpatterns=[
    path("favorite/<int:pk>",views.FavoriteProductView.as_view(),name="favorite")
]