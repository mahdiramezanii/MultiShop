from django.urls import path
from . import views

app_name="Home_app"
urlpatterns=[
    path("",views.Home.as_view(),name="Home"),
    path("product/<slug:slug>",views.DetailProduct.as_view(),name="detail"),
    path("cart",views.ShopCart.as_view(),name="cart"),
    path("cart/delete/<int:pk>",views.DeleteShopCart.as_view(),name="delet")
]

