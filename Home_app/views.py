from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, View, DetailView
from Product_app.models import Product, Category, Comment, Cart, CartDetail
from django.urls import reverse


class Home(View):

    def get(self, request):
        product = Product.objects.all()
        category = Category.objects.all()
        context = {
            "category": category,
            "product": product,
        }

        return render(request, "Home_app/index.html", context=context)


class DetailProduct(DetailView):
    model = Product
    template_name = "Home_app/detail.html"

    def post(self, request, slug):
        product = Product.objects.get(slug=slug)
        user = request.user
        body = request.POST.get("body")
        if user and body is not None:
            Comment.objects.create(user=user, body=body, product=product, name=user.get_full_name(), email=user.email)
            return redirect(reverse("Home_app:detail", kwargs={"slug": slug}))

        else:

            color = request.POST.get("color")
            size = request.POST.get("size")
            count = request.POST.get("count")
            user = request.user

            if Cart.objects.filter(user=user).exists():
                cart = Cart.objects.all().last()
                CartDetail.objects.create(cart=cart, product=product, price=product.price, color=color, size=size,
                                          count=count)
                return redirect("Home_app:Home")

            else:
                cart = Cart.objects.create(user=user)
                CartDetail.objects.create(cart=cart, product=product, price=product.price, color=color, size=size,
                                          count=count)
                return redirect("Home_app:Home")
