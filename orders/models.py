from django.db import models 
from shop.models import Product

class Order(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)  # статус замовлення

    def __str__(self):
        return f'Order {self.id} - {self.full_name}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product.name} x {self.quantity}'

# Модель повідомлень для чату, може бути пов'язана із замовленням
class Message(models.Model):
    sender_name = models.CharField(max_length=100)  # можна ім'я користувача
    content = models.TextField()                     # текст повідомлення
    timestamp = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name='messages')

    def __str__(self):
        return f'{self.sender_name}: {self.content[:30]}'
