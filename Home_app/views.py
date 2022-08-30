from django.shortcuts import render
from django.views.generic import TemplateView,ListView,View
from Product_app.models import Product,Category

class Home(View):

    def get(self,request):
        category=Category.objects.all()
        context={
            "category":category,
        }


        return render(request,"Home_app/index.html",context=context)


