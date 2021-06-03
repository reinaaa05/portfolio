from django.db.models import query
from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
    Products,
)

import os

class ProductListView(LoginRequiredMixin, ListView):
    model = Products
    template_name = os.path.join('stores', 'product_list.html')

    def get_queryset(self):
        query = super().get_queryset()
        product_type_name = self.request.GET.get('product_type_name', None)
        product_name = self.request.GET.get('product_name', None)
        if product_type_name:
            query = query.filter(
                product_type__name=product_type_name
            )

        if product_name:
            query = query.filter(
                name=product_name
            )
        order_by_price = self.request.GET.get('order_by_price', 0)
        if order_by_price=='1':
            query = query.order_by('price')
        elif order_by_price== '2':
            query = query.order_by('-price')
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_type_name'] = self.request.GET.get('product_type_name', '')
        context['product_name'] = self.request.GET.get('product_name', '')
        order_by_price = self.request.GET.get('order_by_price')
        if order_by_price == '1':
            context['ascending'] = True
        elif order_by_price == '2':
            context['descending'] = True
        return context