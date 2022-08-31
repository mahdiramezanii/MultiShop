from django.db import models
from Acount_app.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="product/category")
    parent=models.ForeignKey("self",related_name="comment",on_delete=models.CASCADE,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.name

class Color(models.Model):
    name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name

class Size(models.Model):
    s=[
        ('Larg', 'L'),
        ('Mediom', 'M'),
        ('Small', 'S'),
        ('Xlarg', 'XL'),
        ('XXLarg', 'XXL'),
        ('XXXLarg', 'XXXL'),
    ]
    name=models.CharField(max_length=50,choices=s)


    def __str__(self):
        return self.name

class ProductImageGallery(models.Model):
    image=models.ImageField(upload_to="product/image/gallery")
    created=models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name=models.CharField(max_length=200)
    discription=models.TextField()
    image=models.ImageField(upload_to="product/image")
    price=models.CharField(max_length=50)
    size=models.ManyToManyField(Size,related_name="product")
    color=models.ManyToManyField(Color,related_name="product")
    discount=models.CharField(max_length=50,null=True,blank=True)
    score=models.IntegerField(null=True,default=0)
    category=models.ManyToManyField(Category,related_name="product")
    created=models.DateTimeField(auto_now_add=True)
    image_galeery=models.ManyToManyField(ProductImageGallery,related_name="product")
    slug=models.SlugField(null=True,blank=True)


    def get_absolut_url(self):

        return reverse("Home_app:detail",kwargs={"slug":self.slug})

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)

        super(Product,self).save(*args,**kwargs)

    def __str__(self):

        return self.name


class Comment(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="comment")
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comment")
    name=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    body=models.TextField()
    parent=models.ForeignKey("self",on_delete=models.CASCADE,related_name="replay",null=True,blank=True)
    creted=models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.body[:35]

