from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),       # головна та товарні сторінки
    path('orders/', include('orders.urls')),
    path('chat/', include('chat.urls')),
]
