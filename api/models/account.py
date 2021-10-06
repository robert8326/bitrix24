from django.db import models


class User(models.Model):
    name = models.CharField(verbose_name='first name', max_length=255)
    surname = models.CharField(verbose_name='last name', max_length=255)
    phone = models.CharField(max_length=12, verbose_name="Buyer's phone number", unique=True)
    address = models.CharField(max_length=255, verbose_name="Buyer's address")
