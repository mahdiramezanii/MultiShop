# Generated by Django 4.1 on 2022-09-13 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0034_alter_otc_expiration_date_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otc',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 15, 27, 23, 814507, tzinfo=datetime.timezone.utc)),
        ),
    ]
