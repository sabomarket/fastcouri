# Generated by Django 4.2.3 on 2023-09-26 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0013_remove_step5_user_remove_step6_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tracking_id',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
