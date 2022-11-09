from django.db import models
from django.urls import reverse


class Brand_s(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length = 128, db_index=True)
    description = models.TextField(null=True, blank=True)
    image = models.TextField()

    def get_absolute_url(self):
        return reverse ('brand', kwargs={'brand_id':self.pk})
        
    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
    

class Product_s(models.Model):
    name = models.CharField(max_length = 256)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.TextField()
    category = models.ForeignKey(Brand_s, on_delete=models.CASCADE, null = True)

    def get_absolute_url(self):
        return reverse ('product', kwargs={'prod_id':self.pk})

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    