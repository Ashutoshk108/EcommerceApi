from django.core.cache import cache
from rest_framework import generics, mixins
from .models import Product, Category, Currency
from .serializers import ProductSerializer, CategorySerializer, CurrencySerializer
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from rest_framework.response import Response

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        # Check if the product list is cached
        product_list = cache.get('product_list')
        if product_list:
            return Response(product_list)
        # If not cached, fetch the data and cache it
        response = super().list(request, *args, **kwargs)
        cache.set('product_list', response.data, timeout=60 * 5)  # Cache for 5 minutes
        return response

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        # Check if the product is cached
        product_id = kwargs['pk']
        product = cache.get(f'product_{product_id}')
        if product:
            serializer = self.get_serializer(product)
            return Response(serializer.data)
        # If not cached, fetch the data and cache it
        response = super().retrieve(request, *args, **kwargs)
        cache.set(f'product_{product_id}', response.data, timeout=60 * 5)  # Cache for 5 minutes
        return response

class CategoryListCreateAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        # Check if the category list is cached
        category_list = cache.get('category_list')
        if category_list:
            return Response(category_list)
        # If not cached, fetch the data and cache it
        response = super().list(request, *args, **kwargs)
        cache.set('category_list', response.data, timeout=60 * 5)  # Cache for 5 minutes
        return response

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CategoryRetrieveUpdateDestroyAPIView(mixins.UpdateModelMixin,
                                           mixins.DestroyModelMixin,
                                           generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        # Check if the category is cached
        category_id = kwargs['pk']
        category = cache.get(f'category_{category_id}')
        if category:
            serializer = self.get_serializer(category)
            return Response(serializer.data)
        # If not cached, fetch the data and cache it
        response = super().retrieve(request, *args, **kwargs)
        cache.set(f'category_{category_id}', response.data, timeout=60 * 5)  # Cache for 5 minutes
        return response

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CurrencyListCreateAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    def list(self, request, *args, **kwargs):
        # Check if the currency list is cached
        currency_list = cache.get('currency_list')
        if currency_list:
            return Response(currency_list)
        # If not cached, fetch the data and cache it
        response = super().list(request, *args, **kwargs)
        cache.set('currency_list', response.data, timeout=60 * 5)  # Cache for 5 minutes
        return response

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CurrencyRetrieveUpdateDestroyAPIView(mixins.UpdateModelMixin,
                                           mixins.DestroyModelMixin,
                                           generics.RetrieveAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    def retrieve(self, request, *args, **kwargs):
        # Check if the currency is cached
        currency_id = kwargs['pk']
        currency = cache.get(f'currency_{currency_id}')
        if currency:
            serializer = self.get_serializer(currency)
            return Response(serializer.data)
        # If not cached, fetch the data and cache it
        response = super().retrieve(request, *args, **kwargs)
        cache.set(f'currency_{currency_id}', response.data, timeout=60 * 5)  # Cache for 5 minutes
        return response

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@receiver(post_save, sender=Product)
def clear_product_cache(sender, instance, **kwargs):
    # Clear the cached product list
    cache.delete('product_list')

    # Clear the cached product
    cache.delete(f'product_{instance.id}')

@receiver(post_delete, sender=Product)
def clear_deleted_product_cache(sender, instance, **kwargs):
    # Clear the cached product list
    cache.delete('product_list')

    # Clear the cached product
    cache.delete(f'product_{instance.id}')

@receiver(post_save, sender=Category)
def clear_category_cache(sender, instance, **kwargs):
    # Clear the cached category list
    cache.delete('category_list')

@receiver(post_delete, sender=Category)
def clear_deleted_category_cache(sender, instance, **kwargs):
    # Clear the cached category list
    cache.delete('category_list')

@receiver(post_save, sender=Currency)
def clear_currency_cache(sender, instance, **kwargs):
    # Clear the cached currency list
    cache.delete('currency_list')

@receiver(post_delete, sender=Currency)
def clear_deleted_currency_cache(sender, instance, **kwargs):
    # Clear the cached currency list
    cache.delete('currency_list')
