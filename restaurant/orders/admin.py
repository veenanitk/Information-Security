from django.contrib import admin

# Register your models here.
from orders.models import Customer, Manager, Restaurant, Item, Order, Bill, Feedback

admin.site.register(Customer)
admin.site.register(Manager)
admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Bill)
admin.site.register(Feedback)

