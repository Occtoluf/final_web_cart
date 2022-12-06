from cart.models import Order, OrderLine
from main.models import Product_s, Size, Position


def get_or_create_cart():
    try:
        return Order.objects.get(status='Init')
    except:
        return Order.objects.create(status='Init')


def add_to_cart(cart, request):
    position = Position.objects.filter(
        product=request.POST['product_id'],
        size=request.POST['size']
    ).first()

    try:
        order_line = OrderLine.objects.filter(order=cart, position=position).first()
        if order_line is not None:
            if position.quantity > order_line.number_of_products + 1:
                OrderLine.objects.filter(id=order_line.id).update(
                    number_of_products=order_line.number_of_products + 1,
                    product_price=order_line.product_price + float(position.product.price)
                )
        else:
            raise
    except Exception as e:
        if position.quantity > 0:
            OrderLine.objects.create(order=cart, position=position, number_of_products=1, product_price=position.product.price)


def count_total(order_lines):
    sum = 0
    for line in order_lines:
        sum += line.position.product.price * line.number_of_products
    return sum


def write_off_postions(cart):
    """ Изменяем товар в наличии при покупке"""
    order_lines = OrderLine.objects.filter(order=cart).prefetch_related('position')
    for line in order_lines:
        Position.objects.filter(id=line.position.id).update(quantity=line.position.quantity-line.number_of_products)


