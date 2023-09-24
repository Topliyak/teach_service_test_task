from django.urls import path
from .views import product_lessons, products_lessons, all_products_statistic


urlpatterns = [
    path('product_lessons/<int:product_id>', product_lessons),
    path('products_lessons/', products_lessons),
    path('products_statistic/', all_products_statistic),
]
