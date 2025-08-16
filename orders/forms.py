from django import forms
from .models import Order, Message

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone', 'address']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sender_name', 'content']
