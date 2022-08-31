from django.shortcuts import render
from django.views.generic import TemplateView,ListView,View,DetailView
from Product_app.models import Product,Category

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


