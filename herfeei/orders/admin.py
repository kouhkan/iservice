from django.contrib import admin

from herfeei.orders.models import Order, OrderDateTime

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderDateTime)
