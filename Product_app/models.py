from django.db import models
from Acount_app.models import User


class Category(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="product/category")
    parent=models.ForeignKey("self",related_name="comment",on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.name

class Product(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="product/image")
    price=models.CharField(max_length=50)
    discount=models.CharField(max_length=50,null=True,blank=True)
    score=models.IntegerField(null=True)
    category=models.ManyToManyField(Category,related_name="product")
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.name

