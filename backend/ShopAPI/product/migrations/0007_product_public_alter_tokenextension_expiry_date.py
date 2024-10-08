# Generated by Django 5.1.1 on 2024-09-27 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_user_alter_tokenextension_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='public',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='tokenextension',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 28, 15, 3, 16, 72630, tzinfo=datetime.timezone.utc)),
        ),
    ]
