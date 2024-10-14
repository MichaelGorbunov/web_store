from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from catalog.models import Contact, Product
# from django.core.paginator import Paginator
from catalog.form import Form_Add_Product
from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView
from config.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


# Create your views here.


def send(request):
    return render(request, "catalog/send.html")


class ContactListView(ListView):
    model = Contact
    template_name = 'catalog/contact.html'
    context_object_name = 'contact'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.last()  # вывод первого
    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        name = self.request.POST.get('name')
        phone = self.request.POST.get('phone')
        message = self.request.POST.get('message')


        # send_mail(f'{name} от {phone}', message,
        #           DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)

        return self.render_to_response(context)




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


