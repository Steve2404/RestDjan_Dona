# Generated by Django 5.1.1 on 2024-09-24 15:06

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0004_alter_tokenproxy_options'),
        ('product', '0002_alter_product_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('token_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authtoken.token')),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(2024, 9, 25, 15, 6, 43, 364311, tzinfo=datetime.timezone.utc))),
            ],
            bases=('authtoken.token',),
        ),
    ]
