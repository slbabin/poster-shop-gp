from django.http import HttpResponse

from .models import Order, OrderItem
from products.models import Poster

import json

import time



class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)


    def handle_payment_intent_succeeded(self, event):

        intent = event.data.object

        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
        intent.latest_charge
        )

        billing_details = stripe_charge.billing_details 
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2) 

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:        
                order = Order.objects.get(
                    name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                
                order_exists = True
                break
            
                
                
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)   
        else:           
            try:
                order = Order.objects.create(
                    name=shipping_details.name,
                    email=billing_details.email,
                    phone=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Poster.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                            )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                                order_line_item = OrderItem(
                                    order=order,
                                    poster=product,
                                    quantity=quantity,
                                    poster_size=size,
                                )
                                order_line_item.save()
            except Exception as e:
                if order:

                    order.delete()

                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)    