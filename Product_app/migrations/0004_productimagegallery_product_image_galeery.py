# Generated by Django 4.1 on 2022-08-31 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_app', '0003_color_size_alter_product_score_product_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImageGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/image/gallery')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='image_galeery',
            field=models.ManyToManyField(related_name='product', to='Product_app.productimagegallery'),
        ),
    ]
