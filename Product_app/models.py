from django.db import models
from Acount_app.models import User


class Category(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="product/image")
    parent=models.ForeignKey("self",related_name="comment",on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.name



