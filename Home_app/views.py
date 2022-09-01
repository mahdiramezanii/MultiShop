from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, View, DetailView,DeleteView
from Product_app.models import Product, Category, Comment, Cart, CartDetail
from django.urls import reverse,reverse_lazy


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

        if request.user.is_authenticated:

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

                if color and size and count:

                    if Cart.objects.filter(user=user).exists():
                        cart = Cart.objects.filter(user=user).last()
                        CartDetail.objects.create(cart=cart, product=product, price=product.price, color=color, size=size,
                                          count=count)
                        return redirect(reverse("Home_app:detail", kwargs={"slug": slug}))

                    else:
                        cart = Cart.objects.create(user=user)
                        CartDetail.objects.create(cart=cart,product=product, price=product.price, color=color, size=size,
                                            count=count)
                        return redirect(reverse("Home_app:detail", kwargs={"slug": slug}))

                return redirect(reverse("Home_app:detail", kwargs={"slug": slug}))

        return redirect(reverse("Home_app:detail", kwargs={"slug": slug}))


class ShopCart(ListView):
    model=DetailProduct
    template_name = "Home_app/cart.html"

    def get_queryset(self):
        if self.request.user.is_authenticated:

            if Cart.objects.filter(user=self.request.user).exists():
                cart=Cart.objects.filter(user=self.request.user).last()
                query_set=CartDetail.objects.filter(cart=cart)
                if query_set.exists():
                    return query_set
                return None

        else:
            query_set=None
            return query_set


class DeleteShopCart(DeleteView):
    model = CartDetail
    success_url = reverse_lazy("Home_app:cart")

