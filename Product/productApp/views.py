# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from productApp.models import Product
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class productList(ListView):
    model = Product


class productView(DetailView):
    model = Product

class productCreate(CreateView):
    model = Product
    fields = ['name', 'price']
    success_url = reverse_lazy('product_list')


class productUpdate(UpdateView):
    model = Product
    fields = ['name', 'price']
    success_url = reverse_lazy('product_list')

class productDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')