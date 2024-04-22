"""
->This file defines the Django REST Framework serializers for the ecommerce application models.
->The ProductSerializer, CategorySerializer, and CurrencySerializer classes are used to serialize and deserialize the corresponding model instances.
->These serializers define the fields that should be included in the API response and handle the conversion between Python objects and JSON data.
"""

from rest_framework import serializers
from .models import Product, Category, Currency

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'
        