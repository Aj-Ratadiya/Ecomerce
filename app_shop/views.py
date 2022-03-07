from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product

class Home(ListView):
    model=Product
    template_name='app_shop/home.html'

class ProductDetail(LoginRequiredMixin,ListView):

    model=Product
    template_name='app_shop/productdetail.html'
    context_object_name='product'


    # queryset=Product.objects.all()
    #
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductDetail,
    #          self).get_context_data(*args, **kwargs)
    #     context = context.objects.all()
    #     return context
