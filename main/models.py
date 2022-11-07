from django.db import models

class Brand_s(models.Model):
    name = models.CharField(max_length = 128)
    description = models.TextField(null=True, blank=True)
    image = models.TextField()

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Product_s(models.Model):
    name = models.CharField(max_length = 256)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.TextField()
    category = models.ForeignKey(Brand_s, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
