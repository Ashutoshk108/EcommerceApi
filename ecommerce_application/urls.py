"""
->This file defines the URL patterns for the Django project.
->The urlpatterns list contains the URL routes and the corresponding views that should handle the requests.
->The include function is used to include the URLs from the application app.
"""
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from application.views import (
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    CategoryListCreateAPIView,
    CurrencyListCreateAPIView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Ecommerce Application Api",
        default_version='v1',
        description="Your APIs for managing database for ecommerce application",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
    path('api/categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('api/currencies/', CurrencyListCreateAPIView.as_view(), name='currency-list-create'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
