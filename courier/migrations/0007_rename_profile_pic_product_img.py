# Generated by Django 4.2.3 on 2023-07-26 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0006_product_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='profile_pic',
            new_name='img',
        ),
    ]
