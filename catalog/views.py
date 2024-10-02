from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from catalog.models import Contact,Product
from django.core.paginator import Paginator
from catalog.form import Form_Add_Product
from django.urls import reverse


# Create your views here.


def send(request):
    return render(request, "catalog/send.html")


def contact(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        print(name)
        print(phone)
        print(message)
        data={"name":name}
        # return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
        return render(request, 'catalog/send.html',context=data)

    # contact = Contact.objects.all()
    contact = Contact.objects.first()
    if contact is None:
        data = {"country": "не указано",
                "tax_num": "не указано",
                "address": "не указано",
                "phone": "не указано"
                }

    else:
        data = {"country": contact.country,
                "tax_num": contact.tax_reg_number,
                "address": contact.address,
                "phone": contact.phone
                }
    return render(request, "catalog/contact.html",context=data)

def product_detail(request, product_id):
    # product=Product.objects.get(id=1)
    product = get_object_or_404(Product, pk=product_id)
    data = {
        "product_name": product.name,
        "product_cat": product.category,
        "product_price": product.price,
        "product_descr": product.description,
        "product_img": product.photo,
    }
    # print(data)
    return render(request, "catalog/product_detail.html", context=data)



def base(request):
    return render(request, "catalog/base.html")

def products_list(request):
    products = Product.objects.order_by("-price")
    context = {'products': products}
    return render(request, 'catalog/products_list.html', context)



def add_product(request):
    if request.method == 'POST':
        form = Form_Add_Product(request.POST, request.FILES)
        if form.is_valid():

            # получить данные из формы
            name = form.cleaned_data.get("name")
            description = form.cleaned_data.get("description")
            # photo = form.cleaned_data.get("photo")
            price=form.cleaned_data.get("price")
            category = form.cleaned_data.get("category")
            # создать объект для записи в БД
            obj = Product.objects.create(
                category_id=category.id,
                name=name,
                description=description,
                price=price
                # photo=photo
                )
            # сохранить полученные данные
            obj.save()

            # return HttpResponseRedirect(reverse('products_list2'))
            return HttpResponseRedirect('/catalog/products_list2')

    else:

        form = Form_Add_Product()
        context = {"form": form}
        return render(request, "catalog/add_product.html", context)

# def page_nav(request):
#
#     # products = Product.objects.all()
#     products = Product.objects.order_by("price")
#     paginator = Paginator(products, per_page=2)
#     page_number = request.GET.get('page')
#     page_object = paginator.get_page(page_number)
#     context = {'page_obj': page_object}
#     return render(request, 'catalog/page_nav.html', context)