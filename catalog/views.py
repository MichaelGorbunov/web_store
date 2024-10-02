from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from catalog.models import Contact, Product
# from django.core.paginator import Paginator
from catalog.form import Form_Add_Product
from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView


# Create your views here.


def send(request):
    return render(request, "catalog/send.html")


class ContactListView(ListView):
    model = Contact
    template_name = 'catalog/contact.html'
    context_object_name = 'contact'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.first()  # вывод первого


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/products_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("name")  # сорт по имени


