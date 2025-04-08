from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from .models import *

def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(customer_profile, sender=User)

def product(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='product')
        instance.groups.add(group)
        Product.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(product, sender=User)

def tracking(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='tracking')
        instance.groups.add(group)
        Tracking.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(tracking, sender=User)

def map_image(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='map_image')
        instance.groups.add(group)
        Map_Image.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(map_image, sender=User)

