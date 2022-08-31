from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,View,DetailView
from Product_app.models import Product,Category,Comment
from django.urls import reverse

class Home(View):

    def get(self,request):
        product=Product.objects.all()
        category=Category.objects.all()
        context={
            "category":category,
            "product":product,
        }


        return render(request,"Home_app/index.html",context=context)

class DetailProduct(DetailView):
    model = Product
    template_name = "Home_app/detail.html"

    def post(self,request,slug):
        product=Product.objects.get(slug=slug)
        user=request.user
        body=request.POST.get("body")
        Comment.objects.create(user=user,body=body,product=product)

        return redirect(reverse("Home_app:detail",kwargs={"slug":slug}))




