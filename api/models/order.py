from django.db import models


class Order(models.Model):
    title = models.CharField(max_length=50, verbose_name='Product Name')
    description = models.TextField(verbose_name='Description')
    customer = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='order',
        verbose_name='User'
    )
    product = models.ManyToManyField(
        'Product',
        verbose_name='products',
        related_name='product_order'
    )
    delivery_address = models.CharField(max_length=255, verbose_name="Delivery address")
    delivery_date = models.CharField(max_length=20, verbose_name='Delivery date')
    delivery_code = models.CharField(max_length=50, verbose_name='Delivery code')

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

    def __str__(self):
        return self.title
