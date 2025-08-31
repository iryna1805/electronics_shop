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
        subtotal = product.price * quantity
        total += subtotal
        products.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
    return render(request, 'orders/cart.html', {'products': products, 'total': total})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity', 1))
    cart[str(product_id)] = cart.get(str(product_id), 0) + quantity
    request.session['cart'] = cart
    return redirect('cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart')

def update_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        action = request.POST.get("action")
        if action == "increase":
            cart[str(product_id)] += 1
        elif action == "decrease" and cart[str(product_id)] > 1:
            cart[str(product_id)] -= 1
        request.session['cart'] = cart
    return redirect('cart')


# Оформлення замовлення
def checkout(request):
    cart = request.session.get('cart', {})
    
    cart_products = []
    total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=int(product_id))  
        subtotal = product.price * quantity
        total += subtotal
        cart_products.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    if not cart_products: 
        return redirect('cart')
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart_products:
                OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'])
            request.session['cart'] = {}  # очистка кошика
            return redirect('cart')
    else:
        form = OrderForm()  # форма для GET

    return render(request, 'orders/checkout.html', {'form': form, 'cart_products': cart_products, 'total': total})

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
    return render(request, 'chat/chat.html', {'order': order, 'messages': messages, 'form': form})

