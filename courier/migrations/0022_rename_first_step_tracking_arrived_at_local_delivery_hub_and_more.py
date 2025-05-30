# Generated by Django 5.2 on 2025-04-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0021_rename_expected_arrival_product_pick_up_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracking',
            old_name='first_step',
            new_name='arrived_at_local_delivery_hub',
        ),
        migrations.RenameField(
            model_name='tracking',
            old_name='fourth_step',
            new_name='in_transit_to_destination_city',
        ),
        migrations.RenameField(
            model_name='tracking',
            old_name='second_step',
            new_name='in_transit_to_sorting_facility',
        ),
        migrations.RemoveField(
            model_name='tracking',
            name='third_step',
        ),
        migrations.AddField(
            model_name='tracking',
            name='order_placed',
            field=models.CharField(default='Order Has Been Placed', max_length=200, null=True),
        ),
    ]
