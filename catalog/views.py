from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Contact, Product, Category
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# from config.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from .forms import ProductForm, CategoryForm


# Create your views here.


def send(request):
    return render(request, "catalog/send.html")


class ContactListView(ListView):
    model = Contact
    template_name = "catalog/contact.html"
    context_object_name = "contact"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.last()  # вывод первого

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        name = self.request.POST.get("name")
        phone = self.request.POST.get("phone")
        message = self.request.POST.get("message")

        # send_mail(f'{name} от {phone}', message,
        #           DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)

        return self.render_to_response(context)


class CategoryesListView(ListView):
    model = Category
    template_name = "catalog/categoryes_list.html"
    context_object_name = "categoryes"


class CategoryCreateView(LoginRequiredMixin, CreateView):
    """создание категории продуктов"""

    model = Category
    form_class = CategoryForm
    template_name = "catalog/category_form.html"
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy("catalog:categoryes_list")


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "catalog/category_form.html"
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy("catalog:categoryes_list")


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    """удаление категории"""

    model = Category
    template_name = "catalog/category_confirm_delete.html"
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy("catalog:categoryes_list")


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    login_url = reverse_lazy('users:login')
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductsListView(ListView):
    model = Product
    template_name = "catalog/products_list.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(allowed_publication=True)
        queryset = queryset.order_by("name")
        return queryset


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy("catalog:product_mod_list")

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         # Получение ID пользователя
    #         user_id = request.user.id  # или request.user.pk
    #         return HttpResponse(f"Ваш ID: {user_id}")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy("catalog:product_mod_list")


class ProductModListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "catalog/products_list2.html"
    login_url = reverse_lazy('users:login')
    context_object_name = "products"


class ProductModDetailView(LoginRequiredMixin, DetailView):
    """детальное описание поста"""

    model = Product
    template_name = "catalog/product_detail_mod.html"
    login_url = reverse_lazy('users:login')
    context_object_name = "product"


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """удаление поста"""

    model = Product
    template_name = "catalog/product_confirm_delete.html"
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy("catalog:product_mod_list")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('catalog.delete_product'):
            return HttpResponseForbidden("У вас нет разрешения на удаление этого продукта.")


        return super().dispatch(request, *args, **kwargs)