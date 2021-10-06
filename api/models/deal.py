from django.db import models
from django.contrib.postgres.fields import ArrayField


class Deal(models.Model):
    title = models.CharField(max_length=50, verbose_name='Name deal')
    description = models.TextField(verbose_name='Description')
    client = models.ForeignKey(
        'Client',
        verbose_name='Client',
        on_delete=models.CASCADE,
        related_name='deal',
    )
    products = ArrayField(models.CharField(max_length=255))
    delivery_address = models.CharField(max_length=255, verbose_name="Delivery address")
    delivery_date = models.CharField(max_length=20, verbose_name='Delivery date')
    delivery_code = models.CharField(max_length=50, verbose_name='Delivery code')

    class Meta:
        verbose_name = 'Deal'
        verbose_name_plural = 'Deals'

    def __str__(self):
        return self.title
