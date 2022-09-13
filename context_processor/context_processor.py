from Product_app.models import Cart,CartDetail,Favorite

def count_cart_detail(request):

    if request.user.is_authenticated:

        if Cart.objects.filter(user=request.user).exists():
            cart=Cart.objects.filter(user=request.user).last()
            cart_detail=CartDetail.objects.filter(cart=cart).count()

            return {"detail_count":cart_detail}
        else:
            return {"detail_count":0}
    else:
        return {"detail_count":0}


def count_favorite(request):

    if request.user.is_authenticated:

        if Favorite.objects.filter(user=request.user).exists():
            favorite=Favorite.objects.filter(user=request.user).count()

            return {"favorite_count":favorite}
        else:

            return {"favorite_count": 0}

    else:

        return {"favorite_count":0}