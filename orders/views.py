from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .models import Order, OrderItem, Message
from .forms import OrderForm, MessageForm

# Кошик (сесія)
def cart(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        total += product.price * quantity
        products.append({'product': product, 'quantity': quantity})
    return render(request, 'orders/cart.html', {'products': products, 'total': total})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart')

# Оформлення замовлення
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('index')
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for product_id, quantity in cart.items():
                product = get_object_or_404(Product, id=product_id)
                OrderItem.objects.create(order=order, product=product, quantity=quantity)
            request.session['cart'] = {}  # очистка кошика
            return render(request, 'orders/checkout_success.html', {'order': order})
    else:
        form = OrderForm()
    return render(request, 'orders/checkout.html', {'form': form})

# Чат по замовленню
def order_chat(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    messages = order.messages.all().order_by('timestamp')
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.order = order
            msg.save()
            return redirect('order_chat', order_id=order.id)
    else:
        form = MessageForm()
    return render(request, 'orders/order_chat.html', {'order': order, 'messages': messages, 'form': form})
