from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='shop_index'),  # Головна сторінка
    path('category/<int:category_id>/', views.category_detail, name='shop_category_detail'),
    path('product/<int:product_id>/', views.product_detail, name='shop_product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart')
]