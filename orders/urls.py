from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart/<int:product_id>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('chat/<int:order_id>/', views.order_chat, name='order_chat'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart')
]

