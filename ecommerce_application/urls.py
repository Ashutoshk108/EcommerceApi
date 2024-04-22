"""
->This file defines the URL patterns for the Django project.
->The urlpatterns list contains the URL routes and the corresponding views that should handle the requests.
->The include function is used to include the URLs from the application app.
"""

from django.contrib import admin
from django.urls import path, include
from application.views import (
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    CategoryListCreateAPIView,
    CurrencyListCreateAPIView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
    path('api/categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('api/currencies/', CurrencyListCreateAPIView.as_view(), name='currency-list-create'),
]