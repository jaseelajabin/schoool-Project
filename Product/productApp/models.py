# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})