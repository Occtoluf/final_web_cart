from django.db import models
from main.models import Position
from django.utils.translation import gettext_lazy as _


class ContactInformation(models.Model):
    class Country(models.TextChoices):
        Russia = 'russia', _('Россия')
        Belarus = 'belarus', _('Беларусь')
        Kazakhstan = 'Kazakhstan', _('Казахстан')

    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=255, verbose_name='Отчество')
    country = models.CharField(
        _('Страна'),
        max_length=255,
        choices=Country.choices,
        default=Country.Russia
    )
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.CharField(max_length=100, verbose_name='Email')
    additional = models.TextField(max_length=500, verbose_name='Дополнительная информация')


class Order(models.Model):
    class StatusOrder(models.TextChoices):
        Init = 'init', _('Инициализация')
        In_delivery = 'in_delivery', _('В доставке')
        Done = 'done', _('Выполнен')

    class TypePayment(models.TextChoices):
        Card = 'card', _('Оплата картой')
        Cash = 'cash', _('Наличиными при получении')

    status = models.CharField(
        _('Тип'),
        max_length=100,
        choices=StatusOrder.choices,
        default=StatusOrder.Init
    )

    type_payment = models.CharField(
        _('Тип оплаты'),
        max_length=100,
        choices=TypePayment.choices,
        default=TypePayment.Card
    )

    contact_information = models.ForeignKey(ContactInformation, on_delete=models.CASCADE, blank=True, null=True)


class OrderLine(models.Model):
    """ Позиция в заказе """

    number_of_products = models.IntegerField()
    product_price = models.FloatField()

    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)