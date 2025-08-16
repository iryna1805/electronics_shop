from django.contrib import admin
from .models import Order, OrderItem, Message


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'phone', 'created_at', 'completed')
    inlines = [OrderItemInline]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'content', 'timestamp', 'order')
    list_filter = ('timestamp', 'order')