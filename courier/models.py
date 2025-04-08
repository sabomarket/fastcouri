from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db import models


# Create your models here.
class Customer (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    address = models.CharField (max_length = 200,  null = True)
    phone_number = models.CharField (max_length = 200, null = True)
    country = models.CharField (max_length = 200, null = True)
    city = models.CharField (max_length = 200, null = True)


    def __str__(self):
        return str(self.name)



class Product (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    order = models.CharField (max_length = 200, null = True)
    pick_up_date = models.CharField (max_length = 200,  null = True)
    usps = models.CharField (max_length = 200, null = True)
    destination = models.CharField (max_length = 200, null = True)
    delivery = models.CharField (max_length = 200, null = True)
    package_name = models.CharField (max_length = 200, null = True)
    order_date = models.CharField (max_length = 200, null = True)
    delivery_date = models.CharField (max_length = 200, null = True)
    reciever_name = models.CharField (max_length = 200, null = True)    
    status = models.CharField (max_length = 200, null = True)
    address = models.CharField (max_length = 200, null = True)
    phone_number = models.CharField (max_length = 200, null = True)
    postal_code = models.CharField (max_length = 200, null = True)
    origin = models.CharField (max_length = 200, null = True)
    shipping_amount = models.CharField (max_length = 200, null = True)
    method_of_payment = models.CharField (max_length = 200, null = True, default="Mastercard")
    description = models.CharField (max_length = 200, null = True)
    weight = models.CharField (max_length = 200, null = True, default="12.5Kg")
    service_type = models.CharField (max_length = 200, null = True, default="International")
    tracking_id = models.CharField (max_length = 200, null = True, default="")
    movement = models.CharField (max_length = 200, null = True, default="Hold")
    carrier_reference_number = models.CharField (max_length = 200, null = True)
    quanity = models.CharField (max_length = 200, null = True)
    total_flight = models.CharField (max_length = 200, null = True)
    depature_time = models.CharField (max_length = 200, null = True, default="Processing")
    pick_up_time = models.CharField (max_length = 200, null = True, default="Processing")


    def __str__(self):
        return str(self.name)      

class Map_Image(models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    package_image = models.ImageField (default = "ship.jpg", null = True, blank = True)
    map = models.CharField (max_length = 200,  null = True, default="United State")



    def __str__(self):
        return str(self.name)



order_placed = (
    ('Processing...', 'Processing...'),
    ('Order Has Been Placed', 'Order Has Been Placed'),
    )

sorting_facility = (
    ('Processing...', 'Processing...'),
    ('Order Has Been Sorted', 'Order Has Been Sorted'),
    )

picked_up_by_courier = (
    ('Processing...', 'Processing...'),
    ('Order Has Been Picked Uo For Delivery', 'Order Has Been Picked Uo For Delivery'),
    )




class Tracking (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    order_placed = models.CharField (max_length = 200, null = True, choices = order_placed, default="Order Has Been Placed")
    sorting_facility = models.CharField (max_length = 200,  null = True, choices =sorting_facility, default="Processing...")
    picked_up_by_courier = models.CharField (max_length = 200, null = True, choices = picked_up_by_courier, default="Picked Up by Courier")
    in_transit_to_destination_city = models.CharField (max_length = 200, null = True, default="Processing...")
    arrived_at_local_delivery_hub = models.CharField (max_length = 200, null = True, default="Processing...")
    ready_for_delivery = models.CharField (max_length = 200, null = True, default="Processing...")


    def __str__(self):
        return str(self.name)   

