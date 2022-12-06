from django.core.mail import send_mail
from django.template import loader


def send_notification(order_lines, total, contact_information, pay_method):
    html_message = loader.render_to_string('cart/notification.html', {
        'order_lines': order_lines,
        'total': total,
        'contact_information': contact_information,
        'pay_method': pay_method
    })
    send_mail('New order', 'You get a new order', 'brody0270@mail.ru', ['brody0270@gmail.com'], fail_silently=True,
              html_message=html_message)