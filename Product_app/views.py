from django.shortcuts import render,redirect
from django.views.generic import View
from django.urls import reverse
from Acount_app.models import User
from Product_app.models import Product,Favorite



class FavoriteProductView(View):

    def get(self,request,pk):

        product=Product.objects.get(id=pk)


        if Favorite.objects.filter(user=self.request.user,prodoct=product).exists():
            favorite=Favorite.objects.get(user=request.user,prodoct_id=product.id)
            favorite.delete()


            return redirect(product.get_absolut_url())
        else:
            favorite = Favorite.objects.create(user=request.user, prodoct_id=product.id)


            return redirect(product.get_absolut_url())






