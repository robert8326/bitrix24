from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    price = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        verbose_name='Item amount',
        help_text='Amount in dollars'
    )
    image = models.ImageField(verbose_name='Product picture', upload_to="images/")
    count = models.PositiveIntegerField(verbose_name='Quantity of goods', default=0)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Time of creation')
    updated_at = models.DateField(
        verbose_name='Update time',
        auto_now=True,
        blank=True, null=True
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title
