from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='First name')
    surname = models.CharField(max_length=50, verbose_name='Last name')
    phone = models.CharField(max_length=12, verbose_name='User phone number')
    address = models.CharField(max_length=255, verbose_name='User address')

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name
