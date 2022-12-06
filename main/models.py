from django.db import models
from django.urls import reverse


class Brand_s(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=128, db_index=True)
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
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=0)
    image = models.TextField(null=True)
    image2 = models.TextField(null=True)
    category = models.ForeignKey('Brand_s', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('product', kwargs={ 'id':self.id ,'prod_slug':self.slug})

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Size(models.Model):
    name = models.CharField(max_length=2, verbose_name='Size')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Size'


class Position(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    product = models.ForeignKey(Product_s, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity} {self.product} {self.size}'

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'
