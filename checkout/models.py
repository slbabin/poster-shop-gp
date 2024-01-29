import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Poster
from profiles.models import UserProfile


class Order(models.Model):

    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    order_id = models.CharField(max_length=32, null=False, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=32, null=False, blank=False)
    street_address1 = models.CharField(max_length=255, null=False, blank=False)
    street_address2 = models.CharField(max_length=255, null=False, blank=True)
    city = models.CharField(max_length=255, null=False, blank=False)
    county = models.CharField(max_length=255, null=False, blank=True) 
    country = CountryField(blank_label="Country *", null=False, blank=False) 
    postcode = models.CharField(max_length=255, null=False, blank=True)    
    delivery_price = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    date = models.DateTimeField(auto_now_add=True)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=255, null=False, blank=False, default='')


    def _generate_order_number(self):
        
        return uuid.uuid4().hex.upper()


    def update_total(self):
       
        self.order_total = self.orderitem.aggregate(Sum('order_item_total'))['order_item_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_price = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_price = 0
        self.grand_total = self.order_total + self.delivery_price
        self.save()
        

    def save(self, *args, **kwargs):
        
        if not self.order_id:
            self.order_id = self._generate_order_number()
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.order_id
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='orderitem')
    poster = models.ForeignKey(Poster, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    poster_size = models.CharField(max_length=10, null=False, blank=True)
    order_item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.order_item_total = self.poster.price * self.quantity
        super().save(*args, **kwargs)

    

    def __str__(self):
        return f'SKU {self.poster.sku} on order {self.order.order_id}'