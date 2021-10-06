from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Product name')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title
