from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        verbose_name='Сумма товара',
        help_text='Сумма в долларах'
    )
    image = models.ImageField(verbose_name='Изображение товара', upload_to="images/")
    count = models.PositiveIntegerField(verbose_name='Количество товара', default=0)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateField(
        verbose_name='Время обновления',
        auto_now=True,
        blank=True, null=True
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
