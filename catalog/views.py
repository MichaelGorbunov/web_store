from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from catalog.models import Contact,Product


# Create your views here.
def home(request):

    # products = Product.objects.all()
    #вывод в консоль списка продуктов
    # products = Product.objects.all().order_by('-id')[:5:-1]
    # for product in products:
    #     print(product.name)
    return render(request, "catalog/home.html")

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

def products_list(request):
    products = Product.objects.order_by("name")
    context = {'products': products}
    return render(request, 'catalog/products_list.html', context)

def base(request):
    return render(request, "catalog/base.html")