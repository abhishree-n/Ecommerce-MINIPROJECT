from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Order

@login_required
def create_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == "POST":
        total_price = product.price * 1  # assuming quantity = 1
        Order.objects.create(
            user=request.user,
            product=product,
            quantity=1,
            total_price=total_price
        )
        return redirect('order_success', product_id=product.id)

    return render(request, "orders/confirm_order.html", {"product": product})


@login_required
def order_success(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "orders/order_success.html", {"product": product})


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "orders/my_orders.html", {"orders": orders})
