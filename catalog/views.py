from django.core.exceptions import PermissionDenied
from django.forms import ModelChoiceField
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.core.cache import cache
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Contact, Product, Category
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .services import ProductService
from .forms import CategoriesSelectForm



# from config.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from .forms import ProductForm, CategoryForm, ModeratorProductForm


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

    # def get_context_data(self, **kwargs):
    #     # Получаем стандартный контекст данных из родительского класса
    #     context = super().get_context_data(**kwargs)
    #     cat_id = self.object.id
    #     context['products'] = ProductService.get_prod_from_cat(cat_id)
    #     return context



class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    """удаление категории"""

    model = Category
    template_name = "catalog/category_confirm_delete.html"
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy("catalog:categoryes_list")


@method_decorator(cache_page(60 * 15), name='dispatch')
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
        queryset = cache.get('products_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('products_queryset', queryset, 60 * 15)  # Кешируем данные на 15 минут
        queryset = queryset.filter(allowed_publication=True)
        queryset = queryset.order_by("name")
        return queryset


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy("catalog:product_mod_list")

    def get_form_class(self):
        # Пример: выбор формы в зависимости от пользователя
        if self.request.user.has_perm('catalog.can_unpublish_product'):
            return ModeratorProductForm  # Форма для суперпользователей
        else:
            return ProductForm  # Форма для обычных пользователей


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy("catalog:product_mod_list")

    def get_form_class(self):
        # Пример: выбор формы в зависимости от пользователя
        if self.request.user.has_perm('catalog.can_unpublish_product'):
            return ModeratorProductForm  # Форма для суперпользователей
        else:
            return ProductForm  # Форма для обычных пользователей

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        user = request.user

        # Контрольный список на группу модератора или владельца карточки

        perms_control = [
            user.has_perm('catalog.can_unpublish_product'),
            user.pk == product.owners.pk,
        ]

        # Если есть хотя-бы что-то одно(права или владелец карточки) - изменяем
        if not any(perms_control):
            return HttpResponseForbidden(f'У Вас нет прав для изменения')

        return super().get(self, request, *args, **kwargs)


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
    """удаление продукта"""

    model = Product
    template_name = "catalog/product_confirm_delete.html"
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy("catalog:product_mod_list")

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        user = request.user

        # Контрольный список на группу модератора или владельца карточки

        perms_control = [
            user.has_perm('catalog.can_unpublish_product'),
            user.pk == product.owners.pk,
        ]

        # Если есть хотя-бы что-то одно(права или владелец карточки) - позволить удалить
        if not any(perms_control):
            return HttpResponseForbidden(f'У Вас нет прав для удаления')
        product.delete()
        return redirect('catalog:product_mod_list')


def search_product(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            category = get_object_or_404(Category,name=query_name)
            # results = Product.objects.filter(name__icontains=query_name)
            # results = Product.objects.filter(category=category.pk)
            results = ProductService.get_prod_from_cat(category.pk)
            return render(request, 'catalog/product-search.html', {"results":results})


    return render(request, 'catalog/product-search.html')


def Сategory_products_view(request):
    form = CategoriesSelectForm(request.GET or None)
    products = None

    if form.is_valid() and form.cleaned_data['category']:
        selected_category = form.cleaned_data['category']
        products = ProductService.get_product_by_category(selected_category)  # Use the service function here

    return render(request, 'catalog/category_products.html', {
        'form': form,
        'products': products,
    })