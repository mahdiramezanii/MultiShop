# Generated by Django 4.1 on 2022-08-30 14:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0014_alter_otc_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otc',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 30, 14, 17, 15, 263511, tzinfo=datetime.timezone.utc)),
        ),
    ]
