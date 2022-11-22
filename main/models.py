from django.db import models
from django.urls import reverse


class Brand_s(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length = 128, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(null=True, blank=True)
    image = models.TextField(null=True)
    image2 = models.TextField(null=True)

    def __str__(self):
        return self.name
   

    def get_absolute_url(self):
        return reverse ('brand', kwargs={'brand_slug':self.slug})
        
    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
    

class Product_s(models.Model):
    name = models.CharField(max_length = 256)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=0)
    image = models.TextField(null=True)
    image2 = models.TextField(null=True)
    quantity = models.IntegerField()
    category = models.ForeignKey('Brand_s', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('product', kwargs={'prod_slug':self.slug})

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    