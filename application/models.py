"""
->This file defines the Django models for the ecommerce application.
->The Product model represents a product, with fields for the product name, description, price, and other related information.
->The Category model represents a product category, with fields for the category name and description.
->The Currency model represents a currency, with fields for the currency code and name.
"""
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

class Currency(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=2)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

