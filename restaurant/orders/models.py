from django.db import models
import django.utils.timezone
from django.contrib.auth.models import User

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    owner_id = models.IntegerField(primary_key=True)

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    man_id = models.IntegerField(primary_key=True) 

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cust_id = models.IntegerField(primary_key=True)

class Restaurant(models.Model):
    rest_id = models.IntegerField(primary_key=True, default=1007)
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    man_id = models.ForeignKey(Manager, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='restaurant', default=None)




class Item(models.Model):
    item_id = models.IntegerField(primary_key=True, default=1)
    name = models.CharField(max_length=255)
    cost = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='media/item')
    rest_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=1007)


class Bill(models.Model):
    bill_id = models.IntegerField(primary_key=True, default=2)
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE, default=123)
    rest_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=1007)
    total = models.IntegerField(default=0)


class Order(models.Model):
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE, default=2)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField(default=0)


class Feedback(models.Model):
    feed_back = models.CharField(max_length=255)
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE, default=123)
    rest_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=1007)


class Ad(models.Model):
    ad_id = models.IntegerField(primary_key=True, default=1)

class Offer(models.Model):
    offer_id = models.IntegerField(primary_key=True, default=1)


